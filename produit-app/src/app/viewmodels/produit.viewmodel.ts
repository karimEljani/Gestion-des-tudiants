import { HttpErrorResponse } from "@angular/common/http";
import { Injectable, computed, inject, signal } from "@angular/core";
import { Produit } from "../models/produit.model";
import { ProduitService } from "../services/produit.service";

export type FiltreStock = "TOUS" | "EN_STOCK" | "STOCK_FAIBLE" | "RUPTURE";
export type StatutStock = "rupture" | "faible" | "ok";

@Injectable()
export class ProduitViewModel {
  private readonly produitService = inject(ProduitService);

  readonly seuilStockFaible = 5;

  // ---------- État observé par la vue ----------
  readonly produits = signal<Produit[]>([]);
  readonly chargement = signal(false);
  readonly erreur = signal<string | null>(null);
  readonly message = signal<string | null>(null);

  // Critères de recherche et de filtrage
  readonly recherche = signal("");
  readonly prixMax = signal<number | null>(null);
  readonly filtreStock = signal<FiltreStock>("TOUS");

  // Champs du formulaire (ajout ou modification)
  readonly idEnEdition = signal<number | null>(null);
  readonly libelle = signal("");
  readonly prix = signal<number | null>(null);
  readonly qteStock = signal<number | null>(null);

  // ---------- État dérivé (recalculé automatiquement) ----------
  readonly produitsFiltres = computed(() => {
    const terme = this.recherche().trim().toLowerCase();
    const prixMax = this.prixMax();
    const filtre = this.filtreStock();
    return this.produits().filter((p) => {
      const okLibelle = terme === "" || (p.libelle ?? "").toLowerCase().includes(terme);
      const okPrix = prixMax === null || p.prix <= prixMax;
      const okStock = this.correspondAuFiltre(p, filtre);
      return okLibelle && okPrix && okStock;
    });
  });

  readonly nombreTotal = computed(() => this.produits().length);
  readonly nombreAffiches = computed(() => this.produitsFiltres().length);
  readonly filtresActifs = computed(
    () => this.recherche().trim() !== "" || this.prixMax() !== null || this.filtreStock() !== "TOUS"
  );
  readonly modeEdition = computed(() => this.idEnEdition() !== null);
  readonly formulaireValide = computed(
    () =>
      this.libelle().trim() !== "" &&
      this.prix() !== null && this.prix()! >= 0 &&
      this.qteStock() !== null && this.qteStock()! >= 0
  );

  // ---------- Présentation ----------
  statutStock(p: Produit): StatutStock {
    if (p.qteStock <= 0) return "rupture";
    return p.qteStock < this.seuilStockFaible ? "faible" : "ok";
  }

  // ---------- Actions (appelées par la vue) ----------
  charger(): void {
    this.chargement.set(true);
    this.erreur.set(null);
    this.produitService.getAll().subscribe({
      next: (produits) => {
        this.produits.set(produits);
        this.chargement.set(false);
      },
      error: (err) => this.gererErreur(err),
    });
  }

  enregistrer(): void {
    if (!this.formulaireValide()) return;
    this.message.set(null);
    this.erreur.set(null);

    const produit: Produit = {
      libelle: this.libelle().trim(),
      prix: this.prix()!,
      qteStock: this.qteStock()!,
    };
    const id = this.idEnEdition();
    const requete =
      id === null
        ? this.produitService.create(produit) // POST
        : this.produitService.update(id, produit); // PUT

    requete.subscribe({
      next: () => {
        this.message.set(id === null ? "Produit ajouté." : "Produit modifié.");
        this.annuler();
        this.charger();
      },
      error: (err) => this.gererErreur(err),
    });
  }

  modifier(produit: Produit): void {
    this.message.set(null);
    this.idEnEdition.set(produit.id ?? null);
    this.libelle.set(produit.libelle);
    this.prix.set(produit.prix);
    this.qteStock.set(produit.qteStock);
  }

  annuler(): void {
    this.idEnEdition.set(null);
    this.libelle.set("");
    this.prix.set(null);
    this.qteStock.set(null);
  }

  supprimer(produit: Produit): void {
    if (produit.id === undefined) return;
    this.message.set(null);
    this.erreur.set(null);
    this.produitService.delete(produit.id).subscribe({
      next: () => {
        // Mise à jour locale : inutile de recharger toute la liste
        this.produits.update((liste) => liste.filter((p) => p.id !== produit.id));
        if (this.idEnEdition() === produit.id) this.annuler();
        this.message.set(`Produit « ${produit.libelle} » supprimé.`);
      },
      error: (err) => this.gererErreur(err),
    });
  }

  reinitialiserFiltres(): void {
    this.recherche.set("");
    this.prixMax.set(null);
    this.filtreStock.set("TOUS");
  }

  // ---------- Méthodes privées ----------
  private correspondAuFiltre(p: Produit, filtre: FiltreStock): boolean {
    const statut = this.statutStock(p);
    switch (filtre) {
      case "EN_STOCK":
        return statut !== "rupture";
      case "STOCK_FAIBLE":
        return statut === "faible";
      case "RUPTURE":
        return statut === "rupture";
      default:
        return true;
    }
  }

  private gererErreur(err: HttpErrorResponse): void {
    this.chargement.set(false);
    if (err.status === 0) {
      this.erreur.set("Serveur injoignable : vérifiez que l'application Spring tourne sur le port 8080.");
    } else if (err.status === 404) {
      this.erreur.set("Produit introuvable (404).");
    } else {
      this.erreur.set(`Erreur ${err.status} : ${err.message}`);
    }
  }
}

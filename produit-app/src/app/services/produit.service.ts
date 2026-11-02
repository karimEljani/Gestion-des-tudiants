import { HttpClient } from "@angular/common/http";
import { Injectable, inject } from "@angular/core";
import { Observable } from "rxjs";
import { Produit } from "../models/produit.model";

@Injectable({ providedIn: "root" })
export class ProduitService {
  private readonly http = inject(HttpClient);
  private readonly apiUrl = "/api/produits";

  // GET : récupérer tous les produits
  getAll(): Observable<Produit[]> {
    return this.http.get<Produit[]>(this.apiUrl);
  }

  // GET : récupérer un produit par ID
  getById(id: number): Observable<Produit> {
    return this.http.get<Produit>(`${this.apiUrl}/${id}`);
  }

  // POST : créer un nouveau produit
  create(produit: Produit): Observable<Produit> {
    return this.http.post<Produit>(this.apiUrl, produit);
  }

  // PUT : mettre à jour un produit existant
  update(id: number, produit: Produit): Observable<Produit> {
    return this.http.put<Produit>(`${this.apiUrl}/${id}`, produit);
  }

  // DELETE : supprimer un produit par ID (réponse 204, sans corps)
  delete(id: number): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}/${id}`);
  }
}

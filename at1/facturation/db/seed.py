"""
Remplit la base avec des données de démonstration.
Usage (depuis la racine du projet) :  python -m db.seed
"""
import asyncio
from datetime import date

from sqlmodel import SQLModel, select

import models  # noqa: F401
from db.database import engine, async_session
from models import Client, Article, Facture, LigneFacture, Reglement


async def seed():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

    async with async_session() as s:
        if (await s.execute(select(Client))).first():
            print("Base déjà remplie, rien à faire.")
            return

        s.add_all([
            Client(nom="Ahmed Ben Ali", entreprise="Tech Solutions", ville="Tunis"),
            Client(nom="Sonia Trabelsi", entreprise="Digital Plus", ville="Sfax"),
            Client(nom="Mohamed Tounsi", entreprise="ABC", ville="Sfax"),
            Client(nom="Leila Mansouri", entreprise="Smart Business", ville="Nabeul"),
            Client(nom="Karim Ben Salah", entreprise="Alpha Consulting", ville="Bizerte"),
        ])
        s.add_all([
            Article(designation="Ordinateur Portable", categorie="Informatique", prix_achat=1800, prix_vente=2400, stock=25),
            Article(designation="Écran 24 pouces", categorie="Informatique", prix_achat=350, prix_vente=520, stock=40),
            Article(designation="Souris Optique", categorie="Accessoires", prix_achat=20, prix_vente=45, stock=180),
            Article(designation="Imprimante Laser", categorie="Impression", prix_achat=450, prix_vente=680, stock=18),
            Article(designation="SSD 1 To", categorie="Stockage", prix_achat=180, prix_vente=280, stock=55),
            Article(designation="Routeur WiFi", categorie="Réseau", prix_achat=120, prix_vente=190, stock=35),
            Article(designation="Onduleur 1000VA", categorie="Électricité", prix_achat=220, prix_vente=350, stock=22),
            Article(designation="Clavier mécanique", categorie="Accessoires", prix_achat=60, prix_vente=110, stock=0),
        ])
        await s.commit()

        s.add_all([
            Facture(date_facture=date(2026, 1, 10), echeance=date(2026, 2, 10), statut="Payée", id_client=1),
            Facture(date_facture=date(2026, 1, 15), echeance=date(2026, 2, 15), statut="En attente", id_client=2),
            Facture(date_facture=date(2026, 2, 1), echeance=date(2026, 3, 1), statut="Payée", id_client=3),
            Facture(date_facture=date(2026, 2, 20), echeance=date(2026, 3, 20), statut="Partiellement payée", id_client=4),
            Facture(date_facture=date(2026, 3, 1), echeance=date(2026, 4, 1), statut="En attente", id_client=5),
        ])
        await s.commit()

        s.add_all([
            LigneFacture(quantite=2, prix_vente_ht=2400, taux_tva=19, id_facture=1, id_article=1),
            LigneFacture(quantite=1, prix_vente_ht=520, taux_tva=19, id_facture=2, id_article=2),
            LigneFacture(quantite=2, prix_vente_ht=280, taux_tva=19, id_facture=2, id_article=5),
            LigneFacture(quantite=3, prix_vente_ht=680, taux_tva=19, id_facture=3, id_article=4),
            LigneFacture(quantite=5, prix_vente_ht=190, taux_tva=19, id_facture=4, id_article=6),
            LigneFacture(quantite=4, prix_vente_ht=350, taux_tva=19, id_facture=5, id_article=7),
        ])
        s.add_all([
            Reglement(date=date(2026, 2, 5), montant=5712.0, mode="Virement", id_facture=1),
            Reglement(date=date(2026, 2, 25), montant=500.0, mode="Chèque", id_facture=2),
            Reglement(date=date(2026, 3, 1), montant=2000.0, mode="Virement", id_facture=3),
            Reglement(date=date(2026, 3, 10), montant=500.0, mode="Espèces", id_facture=4),
        ])
        await s.commit()
    print("Base remplie avec les données de démonstration.")


if __name__ == "__main__":
    asyncio.run(seed())

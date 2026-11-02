from typing import Optional
from sqlmodel import SQLModel


class LigneFactureCreate(SQLModel):
    quantite: int
    prix_vente_ht: float
    taux_tva: float
    id_facture: int
    id_article: int


class LigneFactureUpdate(SQLModel):
    quantite: Optional[int] = None
    prix_vente_ht: Optional[float] = None
    taux_tva: Optional[float] = None
    id_facture: Optional[int] = None
    id_article: Optional[int] = None

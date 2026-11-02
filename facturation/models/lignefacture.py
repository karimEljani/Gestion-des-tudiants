from typing import Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from models.facture import Facture
    from models.article import Article


class LigneFacture(SQLModel, table=True):
    id_ligne: Optional[int] = Field(default=None, primary_key=True)
    quantite: int
    prix_vente_ht: float
    taux_tva: float
    id_facture: int = Field(foreign_key="facture.id_facture")
    id_article: int = Field(foreign_key="article.id_article")

    facture: "Facture" = Relationship(back_populates="lignes")
    article: "Article" = Relationship(back_populates="lignes")

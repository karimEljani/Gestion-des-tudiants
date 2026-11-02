from typing import Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from models.lignefacture import LigneFacture


class Article(SQLModel, table=True):
    id_article: Optional[int] = Field(default=None, primary_key=True)
    designation: str
    categorie: Optional[str] = None
    prix_achat: float
    prix_vente: float
    stock: int = 0

    lignes: list["LigneFacture"] = Relationship(back_populates="article")

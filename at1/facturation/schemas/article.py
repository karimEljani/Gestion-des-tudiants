from typing import Optional
from sqlmodel import SQLModel


class ArticleCreate(SQLModel):
    designation: str
    categorie: Optional[str] = None
    prix_achat: float
    prix_vente: float
    stock: int = 0


class ArticleUpdate(SQLModel):
    designation: Optional[str] = None
    categorie: Optional[str] = None
    prix_achat: Optional[float] = None
    prix_vente: Optional[float] = None
    stock: Optional[int] = None

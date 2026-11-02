from typing import Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from models.facture import Facture


class Client(SQLModel, table=True):
    id_client: Optional[int] = Field(default=None, primary_key=True)
    nom: str
    entreprise: Optional[str] = None
    ville: Optional[str] = None

    factures: list["Facture"] = Relationship(back_populates="client")

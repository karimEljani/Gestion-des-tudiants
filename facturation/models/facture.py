from typing import Optional, TYPE_CHECKING
from datetime import date
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from models.client import Client
    from models.lignefacture import LigneFacture
    from models.reglement import Reglement


class Facture(SQLModel, table=True):
    id_facture: Optional[int] = Field(default=None, primary_key=True)
    date_facture: date
    echeance: Optional[date] = None
    statut: Optional[str] = "NON PAYEE"
    id_client: int = Field(foreign_key="client.id_client")

    client: "Client" = Relationship(back_populates="factures")
    lignes: list["LigneFacture"] = Relationship(back_populates="facture")
    reglements: list["Reglement"] = Relationship(back_populates="facture")

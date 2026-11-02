import datetime
from typing import Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from models.facture import Facture


class Reglement(SQLModel, table=True):
    id_reglement: Optional[int] = Field(default=None, primary_key=True)
    # `datetime.date` évite le conflit entre le nom du champ et le type `date`
    date: datetime.date
    montant: float
    mode: Optional[str] = None
    id_facture: int = Field(foreign_key="facture.id_facture")

    facture: "Facture" = Relationship(back_populates="reglements")

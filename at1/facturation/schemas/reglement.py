import datetime
from typing import Optional
from sqlmodel import SQLModel


class ReglementCreate(SQLModel):
    date: datetime.date
    montant: float
    mode: Optional[str] = None
    id_facture: int


class ReglementUpdate(SQLModel):
    date: Optional[datetime.date] = None
    montant: Optional[float] = None
    mode: Optional[str] = None
    id_facture: Optional[int] = None

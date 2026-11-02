from datetime import date
from typing import Optional
from sqlmodel import SQLModel


class FactureCreate(SQLModel):
    date_facture: date
    echeance: Optional[date] = None
    statut: Optional[str] = "NON PAYEE"
    id_client: int


class FactureUpdate(SQLModel):
    date_facture: Optional[date] = None
    echeance: Optional[date] = None
    statut: Optional[str] = None
    id_client: Optional[int] = None

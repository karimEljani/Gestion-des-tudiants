from typing import Optional
from sqlmodel import SQLModel


class ClientCreate(SQLModel):
    nom: str
    entreprise: Optional[str] = None
    ville: Optional[str] = None


class ClientUpdate(SQLModel):
    nom: Optional[str] = None
    entreprise: Optional[str] = None
    ville: Optional[str] = None

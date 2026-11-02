# Charge toutes les classes en mémoire pour que SQLModel.metadata
# connaisse les 5 tables lors du create_all().
from .client import Client
from .article import Article
from .facture import Facture
from .lignefacture import LigneFacture
from .reglement import Reglement

__all__ = ["Client", "Article", "Facture", "LigneFacture", "Reglement"]

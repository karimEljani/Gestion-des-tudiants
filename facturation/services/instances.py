from services.generic_service import CRUDService
from models.client import Client
from models.article import Article
from models.facture import Facture
from models.lignefacture import LigneFacture
from models.reglement import Reglement

client_service = CRUDService(Client)
article_service = CRUDService(Article)
facture_service = CRUDService(Facture)
lignefacture_service = CRUDService(LigneFacture)
reglement_service = CRUDService(Reglement)

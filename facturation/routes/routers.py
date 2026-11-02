from routes.generic_router import make_crud_router
from models.client import Client
from models.article import Article
from models.facture import Facture
from models.lignefacture import LigneFacture
from models.reglement import Reglement
from services.instances import (
    client_service,
    article_service,
    facture_service,
    lignefacture_service,
    reglement_service,
)

router_client = make_crud_router(
    service=client_service, prefix="/clients", tag="Clients",
    model=Client, not_found_msg="Client introuvable",
)
router_article = make_crud_router(
    service=article_service, prefix="/articles", tag="Articles",
    model=Article, not_found_msg="Article introuvable",
)
router_facture = make_crud_router(
    service=facture_service, prefix="/factures", tag="Factures",
    model=Facture, not_found_msg="Facture introuvable",
)
router_lignefacture = make_crud_router(
    service=lignefacture_service, prefix="/lignes-facture", tag="LignesFacture",
    model=LigneFacture, not_found_msg="Ligne de facture introuvable",
)
router_reglement = make_crud_router(
    service=reglement_service, prefix="/reglements", tag="Reglements",
    model=Reglement, not_found_msg="Règlement introuvable",
)

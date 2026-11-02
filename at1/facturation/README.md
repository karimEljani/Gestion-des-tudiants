# Plateforme de facturation intelligente
FastAPI + SQLite (Partie 1) et serveur MCP FastMCP (Atelier 1).

## Arborescence
```
facturation/
├── main.py                  # API FastAPI (lifespan, CORS, routers)
├── db/                      # database.py (engine async) + seed.py (données de démo)
├── models/                  # Client, Article, Facture, LigneFacture, Reglement
├── schemas/                 # schémas Create / Update de chaque ressource
├── services/                # CRUDService générique + instances
├── routes/                  # make_crud_router + routers
├── mcp_server/              # Atelier 1 : serveur MCP (12 tools)
│   ├── server.py
│   ├── api/myApi.py         # couche HTTP (httpx)
│   └── tools/               # articles, clients, analyse_reglements, analyse_clients
├── client/test_client.py    # client MCP de test
├── analytics/               # réservé aux parties suivantes
└── .env
```

## Installation (Windows / PowerShell)
```
python -m pip install uv
python -m uv sync
.venv\Scripts\activate
```
Alternative sans uv :
```
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
```

## Partie 1 : API FastAPI (port 8000)
```
python -m db.seed                # optionnel : données de démonstration
python -m uvicorn main:app --reload
```
Swagger : http://127.0.0.1:8000/docs

## Atelier 1 : serveur MCP (port 8001)
```
cd mcp_server
python server.py
```
URL MCP : http://127.0.0.1:8001/mcp (Postman > MCP, ou `python client/test_client.py`).

Par défaut le serveur MCP interroge l'API Render du TP. Pour utiliser votre API locale,
décommentez `DEPOT_API_URL=http://127.0.0.1:8000` dans `.env`.

## Tools MCP (12)
- Articles : getArticleByID, filterArticlesByPriceRange, searchArticles, getArticleRuptureStock, createArticle
- Clients : getClientByID, searchClients, createClient
- Analyse règlements : analyserReglements, detecterAnomalies
- Analyse clients : top_clients_ca, clients_retard_paiement

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel

import models  # noqa: F401  (enregistre les tables dans SQLModel.metadata)
from db.database import engine
from routes.routers import (
    router_client,
    router_article,
    router_facture,
    router_lignefacture,
    router_reglement,
)


# =========================================================
# LIFESPAN (startup / shutdown)
# =========================================================
@asynccontextmanager
async def lifespan(app: FastAPI):
    # STARTUP
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    yield
    # SHUTDOWN
    await engine.dispose()


# =========================================================
# APP
# =========================================================
app = FastAPI(lifespan=lifespan)

# =========================================================
# CORS CONFIG
# =========================================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # dev only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================================================
# ROUTES
# =========================================================
app.include_router(router_client)
app.include_router(router_article)
app.include_router(router_facture)
app.include_router(router_lignefacture)
app.include_router(router_reglement)


# =========================================================
# HOME
# =========================================================
@app.get("/")
def home():
    return {"message": "Welcome to FastAPI!"}

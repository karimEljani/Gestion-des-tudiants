"""
server.py - point d'entrée du serveur MCP de facturation.
Lancement (depuis le dossier mcp_server) : python server.py
"""
import asyncio
import os

from fastmcp import FastMCP

from tools import (
    articles_tools,
    analyse_clients_tools,
    analyse_reglements_tools,
    clients_tools,
)

mcp_server = FastMCP("Facturation Server")

mcp_server.mount(articles_tools.mcp)
mcp_server.mount(analyse_clients_tools.mcp)
mcp_server.mount(analyse_reglements_tools.mcp)
mcp_server.mount(clients_tools.mcp)

HOST = os.getenv("MCP_HOST", "127.0.0.1")
PORT = int(os.getenv("MCP_PORT", "8001"))
PATH = os.getenv("MCP_PATH", "/mcp")


async def main():
    # Lancer le serveur (bloquant)
    await mcp_server.run_async(
        transport="streamable-http",
        host=HOST,
        port=PORT,
        path=PATH,
    )


if __name__ == "__main__":
    asyncio.run(main())

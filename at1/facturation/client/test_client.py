"""
Petit client MCP de test (FastMCP Client).
Usage (serveur MCP lancé) :  python client/test_client.py
"""
import asyncio
import json
import os

from fastmcp import Client

URL = os.getenv("MCP_URL", "http://127.0.0.1:8001/mcp")


async def main():
    async with Client(URL) as client:
        tools = await client.list_tools()
        print(f"{len(tools)} tools disponibles :")
        for t in tools:
            print(f"  - {t.name}: {t.description}")

        for name, args in [
            ("getArticleRuptureStock", {}),
            ("top_clients_ca", {"top_n": 3}),
            ("detecterAnomalies", {}),
        ]:
            res = await client.call_tool(name, args)
            print(f"\n>>> {name}")
            print(json.dumps(res.data, indent=2, ensure_ascii=False)[:1500])


if __name__ == "__main__":
    asyncio.run(main())

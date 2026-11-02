#!/usr/bin/env bash
# Tests de l API REST (Linux / macOS / Git Bash). L application doit tourner sur le port 8080.
URL=http://localhost:8080/api/produits

echo "--- 1) POST : ajouter un produit"
curl -X POST $URL -H "Content-Type: application/json" \
     -d "{\"libelle\": \"Produit Test\", \"prix\": 100.0, \"qteStock\": 10}"

echo; echo "--- 2) GET : tous les produits"
curl -X GET $URL

echo; echo "--- 3) GET : produit d id 1"
curl -X GET $URL/1

echo; echo "--- 4) PUT : mise a jour du produit 1"
curl -X PUT $URL/1 -H "Content-Type: application/json" \
     -d "{\"libelle\": \"Produit Modifie\", \"prix\": 150.0, \"qteStock\": 25}"

echo; echo "--- 5) DELETE : suppression du produit 1 (attendu : 204)"
curl -i -X DELETE $URL/1

echo; echo "--- 6) GET : produit 1 apres suppression (attendu : 404)"
curl -i -X GET $URL/1

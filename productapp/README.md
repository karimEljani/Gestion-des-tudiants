# TP1 – Architecture MVC avec Spring MVC (productapp)

## Prérequis
- Java 17, Maven (variable Path configurée)
- VS Code + Extension Pack for Java + Spring Boot Extension Pack

## Lancer l application
    mvn spring-boot:run

- Vue MVC (Thymeleaf) : http://localhost:8080/produits
- API REST : http://localhost:8080/api/produits
- Console H2 : http://localhost:8080/h2-console (JDBC URL : jdbc:h2:mem:testdb, user : sa, mot de passe vide)

## Tests de l API avec curl (application lancée)

- Tous les produits : curl -X GET http://localhost:8080/api/produits
- Un produit par ID : curl -X GET http://localhost:8080/api/produits/1
- Ajouter : curl -X POST http://localhost:8080/api/produits -H "Content-Type: application/json" -d "{\"libelle\": \"Produit Test\", \"prix\": 100.0, \"qteStock\": 10}"
- Mettre à jour : curl -X PUT http://localhost:8080/api/produits/1 -H "Content-Type: application/json" -d "{\"libelle\": \"Produit Modifie\", \"prix\": 150.0, \"qteStock\": 25}"
- Supprimer : curl -i -X DELETE http://localhost:8080/api/produits/1

(Sous Windows CMD, les doubles guillemets échappés ci-dessus sont obligatoires ; sous bash on peut aussi utiliser des guillemets simples autour du JSON.)

Scripts fournis : test-api.sh (bash) et test-api.bat (CMD).
Codes attendus : POST 201, GET 200, PUT 200, DELETE 204, ID inexistant 404.

## Remarque sur les versions
Le code du TP utilise javax.persistence, donc le projet est basé sur Spring Boot 2.7.x.
Avec Spring Boot 3.x (défaut de start.spring.io), remplacer javax.persistence par jakarta.persistence.

// src/main/java/com/example/productapp/repository/ProduitRepository.java
package com.example.productapp.repository;

import com.example.productapp.model.Produit;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ProduitRepository extends JpaRepository<Produit, Long> {
}

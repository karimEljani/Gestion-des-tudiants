// src/main/java/com/example/productapp/model/Produit.java
package com.example.productapp.model;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

@Entity
public class Produit {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String libelle;
    private Double prix;
    private Integer qteStock;

    public Produit() {
    }

    public Produit(String libelle, Double prix, Integer qteStock) {
        this.libelle = libelle;
        this.prix = prix;
        this.qteStock = qteStock;
    }

    // Getters et Setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }

    public String getLibelle() { return libelle; }
    public void setLibelle(String libelle) { this.libelle = libelle; }

    public Double getPrix() { return prix; }
    public void setPrix(Double prix) { this.prix = prix; }

    public Integer getQteStock() { return qteStock; }
    public void setQteStock(Integer qteStock) { this.qteStock = qteStock; }
}

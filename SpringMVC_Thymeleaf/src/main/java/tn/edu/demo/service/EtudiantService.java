package tn.edu.demo.service;

import tn.edu.demo.model.Etudiant;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Optional;
import java.util.concurrent.atomic.AtomicLong;

@Service
public class EtudiantService {
    private final List<Etudiant> etudiants = new ArrayList<>();
    private final AtomicLong compteur = new AtomicLong(3);

    public EtudiantService() {
        etudiants.add(new Etudiant(1L, "Karim Eljani", "karim@example.com", "Développement Web"));
        etudiants.add(new Etudiant(2L, "Amira Ben Ali", "amira@example.com", "Réseaux"));
        etudiants.add(new Etudiant(3L, "Youssef Trabelsi", "youssef@example.com", "Multimédia"));
    }

    public List<Etudiant> findAll() {
        return etudiants.stream()
                .sorted(Comparator.comparing(Etudiant::getId))
                .toList();
    }

    public Optional<Etudiant> findById(Long id) {
        return etudiants.stream().filter(e -> e.getId().equals(id)).findFirst();
    }

    public void save(Etudiant etudiant) {
        if (etudiant.getId() == null) {
            etudiant.setId(compteur.incrementAndGet());
            etudiants.add(etudiant);
        } else {
            findById(etudiant.getId()).ifPresent(existing -> {
                existing.setNom(etudiant.getNom());
                existing.setEmail(etudiant.getEmail());
                existing.setSpecialite(etudiant.getSpecialite());
            });
        }
    }

    public void delete(Long id) {
        etudiants.removeIf(e -> e.getId().equals(id));
    }
}

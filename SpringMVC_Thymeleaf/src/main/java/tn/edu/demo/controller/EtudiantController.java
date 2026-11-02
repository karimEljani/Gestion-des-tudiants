package tn.edu.demo.controller;

import jakarta.validation.Valid;
import tn.edu.demo.model.Etudiant;
import tn.edu.demo.service.EtudiantService;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

@Controller
@RequestMapping("/etudiants")
public class EtudiantController {
    private final EtudiantService service;

    public EtudiantController(EtudiantService service) {
        this.service = service;
    }

    @GetMapping
    public String liste(Model model) {
        model.addAttribute("etudiants", service.findAll());
        model.addAttribute("nombreEtudiants", service.findAll().size());
        return "etudiants/liste";
    }

    @GetMapping("/ajouter")
    public String formulaireAjout(Model model) {
        model.addAttribute("etudiant", new Etudiant());
        model.addAttribute("titre", "Ajouter un étudiant");
        return "etudiants/formulaire";
    }

    @PostMapping("/enregistrer")
    public String enregistrer(@Valid @ModelAttribute("etudiant") Etudiant etudiant,
                              BindingResult result,
                              Model model,
                              RedirectAttributes redirectAttributes) {
        if (result.hasErrors()) {
            model.addAttribute("titre", etudiant.getId() == null ? "Ajouter un étudiant" : "Modifier un étudiant");
            return "etudiants/formulaire";
        }
        service.save(etudiant);
        redirectAttributes.addFlashAttribute("message", "Étudiant enregistré avec succès.");
        return "redirect:/etudiants";
    }

    @GetMapping("/modifier/{id}")
    public String formulaireModification(@PathVariable Long id, Model model) {
        Etudiant etudiant = service.findById(id).orElseThrow(() -> new IllegalArgumentException("Étudiant introuvable"));
        model.addAttribute("etudiant", etudiant);
        model.addAttribute("titre", "Modifier un étudiant");
        return "etudiants/formulaire";
    }

    @PostMapping("/supprimer/{id}")
    public String supprimer(@PathVariable Long id, RedirectAttributes redirectAttributes) {
        service.delete(id);
        redirectAttributes.addFlashAttribute("message", "Étudiant supprimé.");
        return "redirect:/etudiants";
    }
}

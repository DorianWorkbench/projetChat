<?php 
    include("modele/Utilisateur.php");

    function connexionUtilisateur($pseudo){
        return Utilisateur::connexionUtilisateur($pseudo);
    }
    function inscriptionUtilisateur($pseudo){
        return Utilisateur::inscriptionUtilisateur($pseudo);
    }
?>
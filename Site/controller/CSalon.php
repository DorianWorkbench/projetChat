<?php
    include("modele/Salon.php");

    function listerSalonUtilisateur($idUtil){
        return Salon::listerSalonUtilisateur($idUtil);
    }

    function creationSalon($nomSalon, $idUtil){
        return Salon::creationSalon($nomSalon, $idUtil);
    }
    function rejoindreSalon($idUtil, $nomSalon){
        return Salon::rejoindreSalon($idUtil, $nomSalon);
    }
?>
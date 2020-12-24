<?php
    include("modele/Message.php");

    function envoyerMessage($texte, $idUtil, $idSalon){
        return Message::envoyerMessage($text, $idUtil, $idSalon);
    }

    function listerMessageServeur($idSalon){
        return Message::listerMessageServeur($idSalon);
    }

?>
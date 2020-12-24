<?php 
include("tools/requetePost.php");

class Utilisateur{
    private $id;
    private $pseudo;

    function __construct($id, $pseudo){
        $this->id = $id;
        $this->pseudo=$pseudo;
    }

    public static function connexionUtilisateur($pseudo){
        
        $pseudo = [
            'pseudo'=> $pseudo
        ];

        $data = requetePost("utilisateurConnexion",$pseudo);

        if($data["data"]["Utilisateur"]["success"] == true){
            
            $id = $data["data"]["Utilisateur"]["id"];
            $pseudo = $data["data"]["Utilisateur"]["pseudo"];
            $utilisateur = new Utilisateur($id, $pseudo);
            
            return $utilisateur;

        }elseif ($data["data"]["Utilisateur"]["success"] == false) {
            return $data["data"]["Utilisateur"]["message"];
        }else{
            return null;
        }  
    }
    public static function inscriptionUtilisateur($pseudo){
        $pseudo = [
            'pseudo'=> $pseudo
        ];

        $data = requetePost("utilisateurInscription",$pseudo);

        return $data["data"]["Utilisateur"]["message"];
    }
    
    public function getInfoUtil(){
        $id = $this->getId();
        $pseudo = $this->getPseudo();
        echo "id : ".$id.' pseudo : '.$pseudo;
    }

    public function getId(){
        return $this->id;
    }
    public function getPseudo(){
        return $this->pseudo;
    }
}
?>
<?php
include("tools/requetePost.php");

class Message{
    private $id;
    private $texte;
    private $dateMessage;
    private $pseudo;
    private $idSalon;

    function __construct($id, $texte, $dateMessage, $pseudo, $idSalon){
        $this->id = $id;
        $this->texte=$texte;
        $this->dateMessage = $dateMessage;
        $this->pseudo = $pseudo;
        $this->idSalon = $idSalon;
    }

    public function getMessage(){
        return $this->texte;
    }
   
    public function getPseudo(){
        return $this->pseudo;
    }
    public function getDateMessage(){
        return $this->dateMessage;
    }
   
   
   
   
    public static function envoyerMessage($texte, $idUtil, $idSalon){
        $infos = [
            'texte'=>$texte,
            'idUtil'=>$idUtil,
            'idSalon'=>$idSalon
        ];

        $data = requetePost("messageEnvoie", $infos);

        if($data["data"]["Message"]["success"] == true){
            return $data["data"]["Message"]["message"];
        }else{
            print("coucou");
            return null;
        }
    }
    public static function listerMessageServeur($idSalon){
        $info = [
            'idSalon'=>$idSalon
        ];

        $listMessageServeur = array();
        $data = requetePost('listeMessageServeur', $info);

        if($data['data']['success'] == true){
            
            
            return $data['data']['Message'];

        }else if($data['data']['success'] == false){
            return $data['data']['message'];
        }else{
            return null;
        }
        
    }

    
}


//Pour rechercher les messages suivant le salon
/*
$data = Message::listerMessageServeur(1);

if(gettype($data) == "string"){
    echo $data;
}else if(gettype($data) == "array"){
    for($i = 0; $i<count($data); $i++){
        echo $data[$i]->getMessage();
    }
}
else{
    echo "erreur";
}
*/
/*
    }*/
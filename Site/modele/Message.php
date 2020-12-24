<?php
include("tools/requetePost.php");

class Message{
    private $id;
    private $texte;
    private $dateMessage;
    private $idUtil;
    private $idSalon;

    function __construct($id, $texte, $dateMessage, $pseudo, $idSalon){
        $this->id = $id;
        $this->texte=$texte;
        $this->dateMessage = $dateMessage;
        $this->idSalon = $idSalon;
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
            for($i = 0; $i<count($data['data']['Message']); $i++){
                $listeMessageServer[] = new Message($data['data']['Message'][$i]['id'], $data['data']['Message'][$i]['message'], $data['data']['Message'][$i]['dateMessage'], $data['data']['Message'][$i]['pseudo'], $idSalon);
            }
            var_dump($listMessageServeur);
            return $listeMessageServer;
        }else if($data['data']['success'] == false){
            return $data['data']['message'];
        }else{
            return null;
        }
        
    }

    public function getMessage(){
        return $this->texte;
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
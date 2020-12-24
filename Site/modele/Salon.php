<?php
    include("tools/requetePost.php");

    class Salon{
        private $id;
        private $nomSalon;
        private $idUtil;

        function __construct($id, $nomSalon, $idUtil){
            $this->id = $id;
            $this->nomSalon=$nomSalon;
            $this->idUtil = $idUtil;
        }

        #Getter/Setter
        public function getId(){
            return $this->id;
        }
        public function getNomSalon(){
            return $this->nomSalon;
        }
        public function getIdUtil(){
            return $this->idUtil;
        }

        
        public static function listerSalonUtilisateur($idUtilisateur){
            $info = [
                'idUtil'=>$idUtilisateur
            ];

            $listeSalon = array();
            $dataSansModif = requetePost('listeServeur', $info);
            $data = $dataSansModif["Salon"];

            if($data == false){
                return $dataSansModif["message"];
            }
            for($i = 0; $i<count($data); $i++){
                $listeSalon[] = new Salon($data[$i]['idServeur'], $data[$i]['nomServeur'], $data[$i]['createurSalon']); 
            }

            return $listeSalon;
        }

        public static function creationSalon($nomSalon, $idUtil){
            $info =[
                'nomSalon'=>$nomSalon,
                'idUtil'=>$idUtil
            ];

            $data = requetePost('creationSalon', $info);

            if($data['data']['Salon']['success'] == true){

                return $data['data']['Salon']['message'];

            }else if($data['data']['Salon']['success'] == false){

                return $data['data']['Salon']['message'];
            
            }else{
                return null;
            }
        }
        public static function rejoindreSalon($idUtil, $nomSalon){
            $info = [
                'idUtil'=>$idUtil,
                'nomSalon'=>$nomSalon
            ];

            $data = requetePost('rejoindreSalon', $info);

            return $data['data']['Salon']['message'];
        }
    }
    //rejoindre un salon puis charger les anciens messages.

    //Condition pour vérifier si l'utilisateur a rejoint un salon et 
    // si oui liste les salons dans lesquels il se trouve

   /* if(gettype(Salon::listerSalonUtilisateur(2))== "string"){
        echo Salon::listerSalonUtilisateur(2);
    }else{
        for ($i=0; $i<count(Salon::listerSalonUtilisateur(2));$i++){
            echo Salon::listerSalonUtilisateur(2)[$i]->getNomSalon();
        }
    }*/

   // echo Salon::listerSalonUtilisateur(2)
//creationSalon
?>
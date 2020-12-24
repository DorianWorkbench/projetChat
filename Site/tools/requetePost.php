<?php
    function requetePost($chemin, $donnee){
        $curl = curl_init("http://localhost:9000/".$chemin);
        curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($curl, CURLOPT_POSTFIELDS, $donnee);

        $dataReq = curl_exec($curl);
        $dataReq = json_decode($dataReq, true);
        return $dataReq;
    }
?>

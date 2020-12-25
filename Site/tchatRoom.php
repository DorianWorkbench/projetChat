<?php
    session_start();

    $idSalon = $_SESSION['idSalon'];
    $pseudoUtilisateur = $_SESSION['utilisateurPseudo'];
    include('controller/CMessage.php');
?>
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chat room</title>
    

</head>
<body>
    <h1>Bienvenue sur le salon</h1>
    <ul id="messages"></ul>
    <input type="text" id="myMessage">
    <button id=sendButton>Send</button>



    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>

    <script src="https://cdn.socket.io/socket.io-3.0.1.min.js"></script>
    <script>
        $(document).ready(function(){

            async function chargementHistorique(){
                var message = await <?php echo json_encode(listerMessageServeur($idSalon),JSON_UNESCAPED_UNICODE) ?>;
                //console.log(typeof(message));
                if(typeof(message)==="string"){
                    $("#messages").append('<li>'+message+'</li>');
                }else{
                    for (let i = 0; i < message.length; i++) {
                    $("#messages").append('<li>'+message[i]['pseudo']+' : '+message[i]['message']+' à '+message[i]['dateMessage']+'</li>');
                } 
                }
                
            }
            

            var idSalon = <?php echo json_encode($idSalon); ?>;
            var nomUtilisateur = <?php echo json_encode($pseudoUtilisateur); ?>;
            var socket = io.connect('http://localhost:9000');
            
            //Sur l'action connect du serveur, une fois executé j'effectue l'action login du même serv.
            socket.on('connect', function(){
                chargementHistorique();
                socket.emit('join', {'data':{'username': nomUtilisateur, 'roomId': idSalon}});
            });

            socket.on('message', function(msg){
                $("#messages").append('<li>'+msg+'</li>');
            });

            $('#sendButton').on('click',function(){
                var idSalon = <?php echo json_encode($idSalon); ?>;
                var idUtil = <?php echo json_encode($_SESSION['utilisateurId']);?>;
                socket.emit('message', {'texte': $('#myMessage').val(), 'idUtil': idUtil, 'idSalon':idSalon});
                $('#myMessage').val('');
            });
        })
        
    </script>
</body>
</html>
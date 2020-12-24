<?php
    session_start();

    $nomSalon = $_SESSION['nomSalon'];
?>
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chat room</title>
    

</head>
<body>
    <h1>Bienvenue sur le salon <?php echo $nomSalon; ?></h1>
    <ul id="messages"></ul>
    <input type="text" id="myMessage">
    <button id=sendButton>Send</button>


    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>

    <script src="https://cdn.socket.io/socket.io-3.0.1.min.js"></script>
    <script>
        $(document).ready(function(){
            var socket = io.connect('http://localhost:9000');
            socket.on('connect', function(){
                console.log("connect");
                socket.send("User connected");
            });
            socket.on('message', function(msg){
                $("#messages").append('<li>'+msg+'</li>');
            });
            $('#sendButton').on('click',function(){
                socket.send($('#myMessage').val());
                $('#myMessage').val('');
            });
        })
        
    </script>
</body>
</html>
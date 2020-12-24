<?php
    session_start();
?>

<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Inscription/Connexion</title>
</head>
<body>
    <h1>Bienvenue sur mon super site de tchat en ligne :</h1>
    <form action="index.php" method="post">
        <input type="text" name="pseudo">
        <button type="submit" name ="btConnexion">Connexion</button>
    </form>
    <form action="index.php" method="post">
        <input type="text" name="pseudoInsc">
        <button type="submit" name = "btInscription">Inscription</button>
    </form>    
    
</body>
</html>



<?php
    include("controller/CUtilisateur.php");

    
    if(isset($_POST['btConnexion'])){
        $utilisateur = connexionUtilisateur($_POST['pseudo']);
        if(gettype($utilisateur) == 'string'){
           echo $utilisateur;
        }else{
            $_SESSION['utilisateurId'] = $utilisateur->getId();
            $_SESSION['utilisateurPseudo'] = $utilisateur->getPseudo();

            header('Location: accueilUtilisateur');
        }
    }
    if(isset($_POST['btInscription'])){
        echo inscriptionUtilisateur($_POST['pseudoInsc']);
    }
?>
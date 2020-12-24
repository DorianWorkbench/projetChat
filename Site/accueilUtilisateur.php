<?php
    session_start();
    
    $utilisateurId = $_SESSION['utilisateurId'];
    $utilisateurPseudo = $_SESSION['utilisateurPseudo'];
    
    include('controller/CSalon.php');

?>

<!-- Mettre le choix des salons que l'utilisateur à rejoint ici. permettre à l'utilisateur de rejoindre un nouveau salon -->
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Choix Salon</title>
</head>
<body>
    <h1>Bienvenue <?php echo $utilisateurPseudo?></h1>

    <h2>Voici vos différents serveurs : </h2>

    <?php
        $listeSalon = listerSalonUtilisateur($utilisateurId);
        if(gettype($listeSalon) == "string"){
            echo $listeSalon;
        }else{
  ?>          <form action="accueilUtilisateur.php" method="post"><?php
            for ($i=0; $i<count($listeSalon);$i++){
?>              <button type="submit" name= "btSalon" value =<?php echo $listeSalon[$i]->getNomSalon();?> > 
                <?php echo $listeSalon[$i]->getNomSalon(); ?> </button>
<?php   

            }
    ?>        </form><?php
        }
    ?>
    <h2>Vous n'avez pas rejoint/créé de serveur ? </h2>
    <form action="accueilUtilisateur" method="post">
        <input type="text" name="nomSalonRejoindre">
        <button type="submit" name = "btSalonRejoindre">Rejoindre</button>
    </form>
    <form action="accueilUtilisateur" method="post">
        <input type="text" name="nomSalonCréé">
        <button type="submit" name="btSalonCree">Créer</button>
    </form>


</body>
</html>

<?php
    if(isset($_POST['btSalon'])){
        $_SESSION['nomSalon']= $_POST['btSalon'];
        header('Location: tchatRoom');
    }

    if(isset($_POST['btSalonRejoindre'])){
        echo rejoindreSalon($utilisateurId, $_POST['nomSalonRejoindre']);
    }
    if(isset($_POST['btSalonCree'])){
        echo creationSalon($_POST['nomSalonCréé'], $utilisateurId);
    }
?>
<?php


?>
<!DOCTYPE HTML PUBLIC> 
<html lang="en"> 
<head> 
    <meta http-equiv="content-type" content="text/html; charset=utf-8"> 
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <link href="https://fonts.googleapis.com/css?family=Special+Elite" rel="stylesheet">
    <link rel="stylesheet" href="css/styles.css">
    <title>Sharp Shooter</title> 
<script>
$(function(){
    $(".ajaxButton").click(function(){
        var message = $(this).attr("data-messageType");
        $.ajax({
            url: "/ajax/ajax.shootGun.php",
            type: "POST", 
            data: {
                messageType: message,
            },
        }).done(function(data){	
            console.log(data);
        });
    });
});
</script>
</head> 
<body> 
    <div id='grid'>
        <div id="colLeft">
            <div class='shadow'>
                <img style="-webkit-user-select: none;" src="http://144.39.210.100:8081/">
            </div>
        </div>
        <div id="colRight" class="centerMe">
            <div id='menu'>
                <h3 style="margin-top:10px;">The Sharp Shooters Present</h3>
                <h1>Exact Strike</h1>
                <button id='bangButton' data-messageType="shoot" class="ajaxButton fill" type="button">Bang!</button>
                <button id='exitButton' data-messageType="exit" class="ajaxButton fill" type="button">Exit</button>
            </div>
        </div>
    </div>
</body> 
</html>
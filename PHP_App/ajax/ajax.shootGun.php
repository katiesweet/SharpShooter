<?php

$message = $_POST['messageType'];
if($message != "shoot" && $message != "exit"){
    echo "bad request: ".$message;
    print_r($_POST);
    exit();
}

$sock = socket_create(AF_INET, SOCK_DGRAM, SOL_UDP);

$len = strlen($message);
socket_sendto($sock, $message, $len, 0, '144.39.210.100', 50000);
socket_close($sock);
echo "sent message";
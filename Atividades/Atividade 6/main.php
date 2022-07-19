<!DOCTYPE html>
<meta charset="UTF-8">
<?php
    $cookie_name = "user";
    $cookie_value = "Miguel";
    setcookie($cookie_name, $cookie_value, time() + (86400 * 30), "/"); // 86400 segundos = 1 dia
?>

<html>
    <head>
        <title>Página Exercício 6</title>
    </head>

    <body>
        <?php
            if(!isset($_COOKIE[$cookie_name])) {
                echo "Cookie chamado '" . $cookie_name . "' não foi definido";
            } else {
                echo "Cookie '" . $cookie_name . "' está definido!<br>";
                echo "Valor: " . $_COOKIE[$cookie_name];
            }
            echo "<br>";

            echo "Hoje é " . date("d/m/Y") .  " e agora são " . date("H:i") . "h" . "<br>";

            $string1 = "olá";
            $string2 = "Mundo";

            echo "string1: " . ($string1). "<br>";
            echo "string2: " . ($string2). "<br>";
            echo "ucfirst($string1): " . ucfirst($string1). "<br>";
            
            teste();

            function teste() {
                echo "Isso é um Teste<br>";
            }

            $arquivo = fopen("contador.txt", "r");
            if(!$arquivo){
                echo "Não consegui abrir o arquivo" ;
            } 
            else { 
                $contador = (int ) fread($arquivo,20); 
                fclose ($arquivo); $contador++; 
                echo" Você é o visitante nº ". $contador .; 
                $arquivo = fopen("contador.txt", "w" ); 
                fwrite($arquivo,$contador); 
                fclose ($arquivo); 
            }
        ?> 
    </body>

</html>
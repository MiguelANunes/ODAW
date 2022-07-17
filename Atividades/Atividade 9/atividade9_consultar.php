<!DOCTYPE html>
<meta charset="UTF-8">

<html>
    <head>
        <title>Atividade 9 - Consulta</title>
    </head>

    <body>
        <?php

            $conexao = mysqli_connect('localhost', 'root', '', 'atividade9');
            if (!$conexao) {
                die('Não consegui conectar: '.mysqli_error());
            }else{
                echo 'Conexão bem sucedida<br>';
            }

        ?>

        <h2>Consultando Registros</h2>

        <?php
            $consulta = "SELECT codigo, nome, mail FROM tabela1";
            $resultado = mysqli_query ($conexao,$consulta);
            echo "codigo - nome - e-mail:<br>";
            while ($linha = mysqli_fetch_row($resultado)){
                echo $linha[0]." - ".$linha[1]." - ".$linha[2]."<br>";
            }
            echo "<br><br>";
        ?>

    </body>

</html>
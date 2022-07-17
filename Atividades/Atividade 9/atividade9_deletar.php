
<!DOCTYPE html>
<meta charset="UTF-8">

<html>
	<head>
		<title>Atividade 9 - Deletar</title>
	</head>

	<body>
		<?php

			$conexao = mysqli_connect('localhost', 'root', '', 'atividade9');
			if (!$conexao) {
				die('Não consegui conectar: '.mysqli_error());
			}else{
				echo 'Conexão bem sucedida';
			}

			$name='';
			$namepreenchido = true;
			
			$email = ''; 
			$emailpreenchido = true;

			if ($_SERVER["REQUEST_METHOD"] == "POST") {

				if (empty($_POST["name"])) {
					$namepreenchido = false;
				}
				if (empty($_POST["mail"])) {
					$emailpreenchido = false;
				}

				if(!$namepreenchido){
					echo "<br>Nome não fornecido<br>";
				} else {     
					$consulta = "DELETE FROM tabela1 WHERE nome='$_POST[name]'";
					$resultado = mysqli_query ($conexao, $consulta);
					mysqli_error($conexao);
					if ($resultado)
						echo "<br>Nome '$_POST[name]' deletado<br>";
					else
						echo "<br>Erro ao deletar o nome <br>";
				}
				if(!$emailpreenchido){
					echo "<br>E-mail nao fornecido<br>";
				} else {
					$consulta = "DELETE FROM tabela1 WHERE mail='$_POST[mail]'";
					$resultado = mysqli_query ($conexao, $consulta);
					mysqli_error($conexao);
					if ($resultado)
						echo "<br>Email '$_POST[mail]' deletado";
					else
						echo "<br>Erro ao deletar o e-mail<br>";
				}
			}

			function limpa_input($input) {
				$input = trim($input);
				$input = stripslashes($input);
				$input = htmlspecialchars($input);
				return $input;
			}

		?>

		<h2>Excluindo Registros</h2>
		<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">  
			delete from tabela1 
			where nome=<input type="text" name="name" placeholder="Nome">

			<br><br>
			delete from tabela1
			where mail=<input type="text" name="mail" placeholder="exemplo@exemplo.com">

			<br><br>
			<input type="submit" name="submit" value="Executar">  
		</form>
		
	</body>

</html>


<!-- 

<!DOCTYPE html>
<meta charset="UTF-8">
<?php
    $cookie_name = "user";
    $cookie_value = "Andre Francisco";
    setcookie($cookie_name, $cookie_value, time() + (86400 * 30), "/"); // 86400 = 1 day   
?>

<html>
<head>
    <title>Melhor página que existe</title>
</head>

<body>
<?php
$name='';
$email='';
$namepreenchido = true;
$emailpreenchido = true;
//=================================================

$conexao = mysqli_connect('localhost', 'root', '', 'udesc');
if (!$conexao) {
    die('Não foi possível conectar: '.mysqli_error());
}
//=================================================

// Check connection
if ($conexao -> connect_errno) {
    echo "Failed to connect to MySQL: " . $mysqli -> connect_error;
    exit();
  }

//$conexao = mysqli_connect('localhost', 'root', '');
//mysqli_select_db($conexao, "udesc");


if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (empty($_POST["name"])) {
        $namepreenchido = false;                // pra não cadastrar no banco de dados se o formulario nao tiver completo
    }
    if (empty($_POST["email"])) {
        $emailpreenchido = false;                // pra não cadastrar no banco de dados se o formulario nao tiver completo
    }
    if($namepreenchido == false){
        echo "Nome não alterado <br>";
    } else {     
        $consulta = "DELETE FROM pessoa WHERE nome='$_POST[name]'";
        $resultado = mysqli_query ($conexao, $consulta);
        mysqli_error($conexao);
        if ($resultado)
            echo "Nome '$_POST[name]' deletado<br>";
        else
            echo "Nome: erro <br>";

        //echo "Nome salvo";
    }
    if($emailpreenchido == false){
        echo "Email nao alterado";
    } else {
        $consulta = "DELETE FROM pessoa WHERE email='$_POST[email]'";
        $resultado = mysqli_query ($conexao, $consulta);
        mysqli_error($conexao);
        if ($resultado)
            echo "Email '$_POST[email]' deletado";
        else
            echo "Email: erro";
    }
}


?>

<h2>Excluir um cadastro</h2>
<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">  

    delete from pessoa 
    where nome=<input type="text" name="name" value="<?php echo $name;?>">

<br><br>
    delete from pessoa 
    where email=<input type="text" name="email" value="<?php echo $email;?>">

  <br><br>
  <input type="submit" name="submit">  
  <input type="reset" name="reset">
</form>


 -->
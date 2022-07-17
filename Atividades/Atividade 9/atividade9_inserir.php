
<!DOCTYPE html>
<meta charset="UTF-8">

<html>
	<head>
		<title>Atividade 9 - Inserção</title>
	</head>

	<body>
		<?php

			$conexao = mysqli_connect('localhost', 'root', '', 'atividade9');
			if (!$conexao) {
				die('Não consegui conectar: '.mysqli_error());
			}else{
				echo 'Conexão bem sucedida';
			}

			$name = ""; 
			$nameErr = "";
			
			$email = ""; 
			$emailErr = "";
			
			$preenchido = false;
			$valido = true;


			if ($_SERVER["REQUEST_METHOD"] == "POST") {
				if (empty($_POST["name"])) {
					$nameErr = "Esse campo é necessário.";
				} else {
					$name = limpa_input($_POST["name"]);
					// verificando se o nome contem apenas letras
					if (!preg_match("/^[a-zA-Z-' ]*$/",$name)) {
					$nameErr = "Nomes apenas podem conter letras e espaços.";
					$valido = false;
					}
				}
			  
				if (empty($_POST["email"])) {
					$emailErr = "Esse campo é necessário.";
				} else {
					$email = limpa_input($_POST["email"]);
					if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
					  $emailErr = "O e-mail está inválido.";
					  $valido = false;
					}
				}
				
				if(!(empty($_POST["email"]) && empty($_POST["name"])) && $valido){
					$preenchido = true;
				}

				if(!$preenchido){
					echo "Dados incompletos";
				} else {
					$consulta = "INSERT INTO tabela1 (nome, mail) values ('$_POST[name]','$_POST[email]')";
					$resultado = mysqli_query ($conexao, $consulta);
					if ($resultado)
						echo "<br>Sucesso ao inserir";
					else
						echo "<br>Erro ao inserir";
				}

			}

			function limpa_input($input) {
			$input = trim($input);
			$input = stripslashes($input);
			$input = htmlspecialchars($input);
			return $input;
			}

		?>

		<h2>Inserindo Registros</h2>
		<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">  
			Nome: <input type="text" name="name" placeholder="Nome Exemplo">
				<span class="error"> <?php echo $nameErr;?></span>
				<br><br>

			E-mail: <input type="text" name="email" placeholder="exemplo@exemplo.com">
				<span class="error"> <?php echo $emailErr;?></span>
				<br><br>

		  <br><br>
		  <input type="submit" name="submit" value="Inserir">    
		</form>
		
	</body>

</html>

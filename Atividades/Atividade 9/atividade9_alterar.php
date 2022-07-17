
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
				echo 'Conexão bem sucedida<br>';
			}

			$name='';
			$novoname='';
			$nameErr = '';
			$namepreenchido = false;
			
			$email = ''; 
			$emailErr = '';
			$novoemail='';
			$emailpreenchido = false;
			
			$valido = true;


			if ($_SERVER["REQUEST_METHOD"] == "POST"){

				if (empty($_POST["novoname"])) {
					$novonameErr = "Campo não fornecido";
					$namepreenchido = false;
				} else {
					$novoname = limpa_input($_POST["novoname"]);
					$namepreenchido = true;
					if (!preg_match("/^[a-zA-Z-' ]*$/",$novoname)) {
						$novonameErr = "Nomes apenas podem conter letras e espaços.";
						$namepreenchido = false;
						$valido = false;
					}
				}
			  
				if (empty($_POST["novoemail"])) {
					$novoemailErr = "Campo não fornecido";
					$emailpreenchido = false;
				} else {
					$novoemail = limpa_input($_POST["novoemail"]);
					$emailpreenchido = true;
					if (!filter_var($novoemail, FILTER_VALIDATE_EMAIL)) {
					  $novoemailErr = "O e-mail está inválido.";
					  $emailpreenchido = false;
					  $valido = false;
					}
				}

				if($namepreenchido == false){
					echo "<br>Nome não alterado <br>";
				} else {     
					$consulta = "UPDATE tabela1 SET nome='$_POST[novoname]' WHERE nome='$_POST[name]'";
					$resultado = mysqli_query ($conexao, $consulta);
					mysqli_error($conexao);
					if ($resultado)
						echo "<br>Nome '$_POST[name]' alterado para '$_POST[novoname]'<br>";
					else
						echo "<br>Erro ao inserir o nome <br>";
			
				}
				if($emailpreenchido == false){
					echo "<br>E-mail nao alterado";
				} else {
					$consulta = "UPDATE tabela1 SET mail='$_POST[novoemail]' WHERE mail='$_POST[email]'";
					$resultado = mysqli_query ($conexao, $consulta);
					mysqli_error($conexao);
					if ($resultado)
						echo "<br>Email '$_POST[email]' alterado para '$_POST[novoemail]'";
					else
						echo "<br>Erro ao inserir o e-mail";
				}
			}

		function limpa_input($input) {
		  $input = trim($input);
		  $input = stripslashes($input);
		  $input = htmlspecialchars($input);
		  return $input;
		}

		?>

		<h2>Alterar um Registro</h2>
		<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">  

			update tabela1 set 
			nome= <input type="text" name="novoname" placeholder="Nome Exemplo">
			where nome=<input type="text" name="name" placeholder="Novo Nome">
			<span class="error"> <?php echo $nameErr;?></span>

			<br><br>
			update tabela1 set 
			mail= <input type="text" name="novoemail" placeholder="exemplo@exemplo.com">
			where mail=<input type="text" name="email" placeholder="novo_email@exemplo.com">
			<span class="error"> <?php echo $emailErr;?></span>

		<br><br>
			<input type="submit" name="submit" value="Executar">  
		</form>
		
	</body>

</html>

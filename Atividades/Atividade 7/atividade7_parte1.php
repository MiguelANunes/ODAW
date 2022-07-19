
<!DOCTYPE html>
<meta charset="UTF-8">
<?php
    $cookie_name = "usuário";
    $cookie_value = "Miguel";
    setcookie($cookie_name, $cookie_value, time() + (86400 * 30), "/"); // 86400 segundos = 1 dia
?>

<html>
<head>
    <title>Exercício 7 ODAW Parte 1 e 3</title>
</head>

<body>
	<?php
		
		$name = ""; 
		$nameErr = "";
		
		$email = ""; 
		$emailErr = "";
		
		$senha = ""; 
		$senhaErr = "";

		if ($_SERVER["REQUEST_METHOD"] == "POST") {
			if (empty($_POST["name"])) {
			    $nameErr = "Esse campo é necessário.";
			} else {
			    $name = limpa_input($_POST["name"]);
			    // verificando se o nome contem apenas letras
			    if (!preg_match("/^[a-zA-Z-' ]*$/",$name)) {
			    $nameErr = "Nomes apenas podem conter letras e espaços.";
			    }
			}
		  
			if (empty($_POST["email"])) {
			    $emailErr = "Esse campo é necessário.";
			} else {
			    $email = limpa_input($_POST["email"]);
			    // verificando se o e-mail é válido
			    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
			      $emailErr = "O e-mail está inválido.";
			    }
			}
			// testando a senha 
			$uppercase    = preg_match('@[A-Z]@', $senha);
			$lowercase    = preg_match('@[a-z]@', $senha);
			$number       = preg_match('@[0-9]@', $senha);

			if (empty($_POST["senha"])) {
			    $senhaErr = "Esse campo é necessário.";
			} else {
			    $senha = limpa_input($_POST["senha"]);

			    if(!$uppercase || !$lowercase || !$number || strlen($password) < 8) {
				$senhaErr = "A senha precisa ter 8 caracteres, pelo menos uma letra maiúscula, uma minúscula e um número.";
			    }
			}

			if (empty($_POST["email"]) || empty($_POST["senha"])) {
			    $preenchido = false;
			    echo $preenchido;
			} else {
			    $preenchido = true;
			}
			
			if($preenchido == false){
			    echo "Formulário Não Preenchido";
			} else{
				
				$arquivo = fopen("autenticador.txt", "a");				

				if(!$arquivo){
					echo "Não consegui abrir o arquivo de autenticação<br>";
				}else{
				
					echo "Email e senha salvos<br>";			
					$senhaHash = password_hash($senha, PASSWORD_DEFAULT);

					fwrite($arquivo, "\n");
					fwrite($arquivo, $email);
					fwrite($arquivo, "-");
					fwrite($arquivo, $senhaHash);
					fclose($arquivo);
				}
			}
		}


		function limpa_input($input) {
		  $input = trim($input);
		  $input = stripslashes($input);
		  $input = htmlspecialchars($input);
		  return $input;
		}
	?>

	<h2>Formulário</h2>

		<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">  
			Nome: <input type="text" name="name" value="<?php echo $name;?>">
			    <span class="error"> <?php echo $nameErr;?></span>
			    <br><br>

			e-mail: <input type="text" name="email" value="<?php echo $email;?>">
			    <span class="error"> <?php echo $emailErr;?></span>
			    <br><br>
			    
			<p>A senha precisa ter 8 caracteres, pelo menos uma letra maiúscula, uma minúscula e um número.</p>
			
			Senha: <input type="password" name="senha">
			    <span class="error"> <?php echo $senhaErr;?></span>
			    <br><br>
		  
		  
			<br><br>
			<input type="submit" name="submit">  
			<input type="reset" name="reset">
		</form>
	</body>

</html>

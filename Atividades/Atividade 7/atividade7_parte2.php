
<!DOCTYPE html>
<meta charset="UTF-8">
<?php
    $cookie_name = "usuário";
    $cookie_value = "Miguel";
    setcookie($cookie_name, $cookie_value, time() + (86400 * 30), "/"); // 86400 segundos = 1 dia
?>

<html>
	<head>
		<title>Exercício 7 ODAW Parte 2</title>
	</head>

	<body>
		<?php

			$email = ""; 
			$emailErr = "";
			
			$senha = ""; 
			$senhaErr = "";
			
			$msg = "";
			
			if ($_SERVER["REQUEST_METHOD"] == "POST") {
				$userN = $_POST["email"];
				$password = $_POST["senha"];
				$userlist = file ("autenticador.txt");

				$email = "";
				$senha = "";
				
				$sucesso = false;
			 
				foreach ($userlist as $user) {
					$user_details = explode("-", $user);

					if ($user_details[0] == $userN && password_verify($password , $user_details[1])) {
						$sucesso = true;
						break;
					}
				}
				
				if ($success) {
					$msg = "Login feito com Sucesso!";
				} else {
					$msg = "Falha no login!";
				}
				
			}
			function limpa_input($input) {
			  $input = trim($input);
			  $input = stripslashes($input);
			  $input = htmlspecialchars($input);
			  return $input;
			}

		?>

		<h2>Login</h2>
		<p><span class="error"></span></p>
		<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">  
			Email: <input type="text" name="email" value="<?php echo $email;?>">
				
			<br><br>

			Senha: <input type="password" name="senha">
				
			<br><br>
			<input type="submit" name="submit">  
			<br><br>
			<span> <?php echo $msgLogin;?></span>
		</form>


	</body>

</html>

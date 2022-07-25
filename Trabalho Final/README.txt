Equipe: Miguel e Daniella

Instruções de Compilação e Execução:
	0: Devido ao fato de termos usado o cliente remoto do MongoDB para o trabalho, 
		o professor poderá apenas executar o sistema dentro da Udesc, já que o IP
		da Udesc está na lista de IPs permitidos do cliente remoto do MongoDB
	1: Executar:
		pip3 install virtualenv 
	   Para instalar o pacote virtualenv do Python
	2: Acessar a pasta sitehandler/ e executar o comando:
		source bin/activate
	3: Executar, dentro da pasta sitehandler/:
		pip3 install -r requirements.txt
	   Para instalar as depedências do projeto
	4: Executar:
		python3 manage.py runserver
	   Para rodar o projeto

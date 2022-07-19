// https://stackoverflow.com/questions/66457318/highlight-text-temporarily
// https://stackoverflow.com/questions/27656634/button-display-inline-css
// clicar para esconder uma seção

var coll = document.getElementsByClassName("collapsible");
var i;

	for (i = 0; i < coll.length; i++) {
		coll[i].addEventListener("click", function() {
			this.classList.toggle("active");
			var content = this.nextElementSibling;
			if (content.style.maxHeight){
				content.style.maxHeight = null;
			}else{
				content.style.maxHeight = content.scrollHeight + "px";
			} 
		});
	}

var data = new Date();
document.getElementById("hoje").innerHTML = data.toLocaleDateString();

function checa_mail() {
	document.getElementById("resultado_mail").innerHTML = "<p></p>";
	var mail = document.getElementById("email").value;
	if (!(mail.includes("@") && (mail.includes(".com") || mail.includes(".br") || mail.includes("edu")))) {
		document.getElementById("resultado_mail").innerHTML = "O e-mail é inválido";
	}else{
		document.getElementById("resultado_mail").innerHTML = "O e-mail é válido";
	}
}

function testa_cpf(cpf) {
	var soma = 0;
	var resto;
	for (var i = 1; i <= 9; i++) {
		soma = soma + parseInt(cpf.substring(i - 1, i)) * (11 - i);
	}
	resto = (soma * 10) % 11;
	if ((resto == 10) || (resto == 11)) {
		resto = 0;
	}
	if (resto != parseInt(cpf.substring(9, 10))) {
		return false;
	}
	soma = 0;
	for (var i = 1; i <= 10; i++) {
		soma = soma + parseInt(cpf.substring(i - 1, i)) * (12 - i);
	}
	resto = (soma * 10) % 11;
	if ((resto == 10) || (resto == 11)) {
		resto = 0;
	}
	if (resto != parseInt(cpf.substring(10, 11))) {
		return false;
	}
	return true;
}

function checa_cpf(){
	cpf = document.getElementById("cpf").value;

	if(!(testa_cpf(cpf))){
		document.getElementById("resultado_cpf").innerHTML = "O CPF é inválido";
	}else{
		document.getElementById("resultado_cpf").innerHTML = "O CPF é válido";
	}
}

function checa_idade(){
	idade = document.getElementById("idade").value;

	if(idade.match(/^[0-9]+$/) == null){
		document.getElementById("resultado_idade").innerHTML = "A idade é inválida";
	}else{
		document.getElementById("resultado_idade").innerHTML = "A idade é válida";
	}
}

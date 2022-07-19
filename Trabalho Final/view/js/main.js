//----------------------------------------------

var buttonAviao = document.getElementById("salvarAviao")
var buttonControlador = document.getElementById("salvarControlador")
var buttonModelo = document.getElementById("salvarModelo")
var buttonSindicato = document.getElementById("salvarSindicato")
var buttonTecnico = document.getElementById("salvarTecnico")
var buttonTeste = document.getElementById("salvarTeste")

//----------------------------------------------

const url = new URLSearchParams(location.search)
const urlGuid = url.get("guid")

//----------------------------------------------

const inputs = document.querySelectorAll(".input")

function addcl(){
	let parent = this.parentNode.parentNode
	parent.classList.add("focus")
}

function remcl(){
	let parent = this.parentNode.parentNode
	if(this.value == ""){
		parent.classList.remove("focus")
	}
}

inputs.forEach(input => {
	input.addEventListener("focus", addcl)
	input.addEventListener("blur", remcl)
})

//----------------------------------------------

async function saveAviao() {
     if (location.search === ''){
          await aviaoService.add()
          .then(res => res)
               .catch(rej => console.log(rej));
          window.location = "aviao.html";
     } else{
          saveUpdateAviao(urlGuid)
          window.location = "aviao.html";
     }
} buttonAviao.addEventListener("click", saveAviao)

async function saveControlador() {
     if (location.search === ''){
          await controladorService.add()
          .then(res => res)
               .catch(rej => console.log(rej));
          window.location = "controlador.html";
     } else{
          saveUpdateControlador(urlGuid)
          window.location = "controlador.html";
     }
} buttonControlador.addEventListener("click", saveControlador)

async function saveModelo() {
     if (location.search === ''){
          await modeloService.add()
          .then(res => res)
               .catch(rej => console.log(rej));
          window.location = "modelo.html";
     } else{
          saveUpdateModelo(urlGuid)
          window.location = "modelo.html";
     }
} buttonModelo.addEventListener("click", saveModelo)

async function saveSindicato() {
     if (location.search === ''){
          await sindicatoService.add()
          .then(res => res)
               .catch(rej => console.log(rej));
          window.location = "sindicato.html";
     } else{
          saveUpdateSindicato(urlGuid)
          window.location = "sindicato.html";
     }
} buttonSindicato.addEventListener("click", saveSindicato)

async function saveTecnico() {
     if (location.search === ''){
          await tecnicoService.add()
          .then(res => res)
               .catch(rej => console.log(rej));
          window.location = "tecnico.html";
     } else{
          saveUpdateTecnico(urlGuid)
          window.location = "tecnico.html";
     }
} buttonTecnico.addEventListener("click", saveTecnico)

async function saveTeste() {
     if (location.search === ''){
          await testeService.add()
          .then(res => res)
               .catch(rej => console.log(rej));
          window.location = "teste.html";
     } else{
          saveUpdateTecnico(urlGuid)
          window.location = "teste.html";
     }
} buttonTeste.addEventListener("click", saveTeste)

//função que preenche os campos do formulário com as informações
//já existentes

async function getExistentInfoAviao() {
     var aviaoToBeUpdated = await aviaoService.searchById(urlGuid)
     .then(res => res.json())
     .catch(rej => console.log(rej))
     
     document.getElementById("coda").value = aviaoToBeUpdated.coda;
     document.getElementById("codm").value = aviaoToBeUpdated.codm;
     
}

async function getExistentInfoControlador() {
     var controladorToBeUpdated = await controladorService.searchById(urlGuid)
     .then(res => res.json())
     .catch(rej => console.log(rej))
     
     var data = controladorToBeUpdated.data.split("/", 3)
     
     document.getElementById("matricula").value = controladorToBeUpdated.matricula;
     document.getElementById("nromembro").value = controladorToBeUpdated.nromembro;
     document.getElementById("cods").value = controladorToBeUpdated.cods;
     document.getElementById("nome").value = controladorToBeUpdated.nome;
     document.getElementById("day").value = data[0];
     document.getElementById("month").value = data[1];
     document.getElementById("year").value = data[2];
     
}

async function getExistentInfoModelo() {
     var modeloToBeUpdated = await modeloService.searchById(urlGuid)
     .then(res => res.json())
     .catch(rej => console.log(rej))
     
     document.getElementById("codm").value = modeloToBeUpdated.codm;
     document.getElementById("nome").value = modeloToBeUpdated.nome;
     document.getElementById("capacidade").value = modeloToBeUpdated.capacidade;
     document.getElementById("peso").value = modeloToBeUpdated.peso;
     document.getElementById("limite").value = modeloToBeUpdated.limite;     
}

async function getExistentInfoSindicato() {
     var sindicatoToBeUpdated = await sindicatoService.searchById(urlGuid)
     .then(res => res.json())
     .catch(rej => console.log(rej))
     
     document.getElementById("cods").value = sindicatoToBeUpdated.cods;
     document.getElementById("nome").value = sindicatoToBeUpdated.nome;
}

async function getExistentInfoTecnico() {
     var tecnicoToBeUpdated = await tecnicoService.searchById(urlGuid)
     .then(res => res.json())
     .catch(rej => console.log(rej))
     
     document.getElementById("matricula").value = tecnicoToBeUpdated.matricula;
     document.getElementById("nromembro").value = tecnicoToBeUpdated.nromembro;
     document.getElementById("codm").value = tecnicoToBeUpdated.codm;
     document.getElementById("cods").value = tecnicoToBeUpdated.cods;
     document.getElementById("endereco").value = tecnicoToBeUpdated.endereco;
     document.getElementById("telefone").value = tecnicoToBeUpdated.telefone;
     document.getElementById("salario").value = tecnicoToBeUpdated.salario;
     document.getElementById("nome").value = tecnicoToBeUpdated.nome;
     
}

async function getExistentInfoTeste() {
     var testeToBeUpdated = await testeService.searchById(urlGuid)
     .then(res => res.json())
     .catch(rej => console.log(rej))

     var data = testeToBeUpdated.data.split("/", 3)
     
     document.getElementById("codt").value = testeToBeUpdated.codt;
     document.getElementById("codm").value = testeToBeUpdated.codm;
     document.getElementById("hora").value = testeToBeUpdated.hora;
     document.getElementById("pontuacao").value = testeToBeUpdated.pontuacao;
     document.getElementById("day").value = data[0];
     document.getElementById("month").value = data[1];
     document.getElementById("year").value = data[2];
}

//----------------------------------------------
//----------------------------------------------

function saveUpdateAviao(urlGuid){
     var url = new URLSearchParams(location.search)
     var urlGuid = url.get("id")
     
     var updateIndex = tempAviaoList.findIndex(aviaos => aviaos.id == urlGuid)
     var editedAviao = tempAviaoList[updateIndex]
     console.log(editedAviao)
     
     editedAviao.coda = document.getElementById("coda").value
     editedAviao.codm = document.getElementById("codm").value

     tempAviaoList[updateIndex] = editedAviao
     
     localStorage.setItem("aviaos", JSON.stringify(tempAviaoList))
     
}

function saveUpdateControlador(urlGuid){
     var url = new URLSearchParams(location.search)
     var urlGuid = url.get("id")
     
     var updateIndex = tempUserList.findIndex(controlador => controlador.id == urlGuid)
     var editedControlador = tempControladorList[updateIndex]
     console.log(editedControlador)
     
     editedControlador.matricula = document.getElementById("matricula").value
     editedControlador.nromembro = document.getElementById("nromembro").value
     editedControlador.cods = document.getElementById("cods").value
     editedControlador.nome = document.getElementById("nome").value
     editedControlador.data = document.getElementById("day").value + "/" + document.getElementById("month").value + "/" + document.getElementById("year").value
     tempControladorList[updateIndex] = editedControlador
     
     localStorage.setItem("controlador", JSON.stringify(tempControladorList))
     
}

function saveUpdateModelo(urlGuid){
     var url = new URLSearchParams(location.search)
     var urlGuid = url.get("id")
     
     var updateIndex = tempModeloList.findIndex(modelos => modelos.id == urlGuid)
     var editedModelo = tempModeloList[updateIndex]
     console.log(editedModelo)
     
     editedModelo.nome = document.getElementById("nome").value
     editedModelo.codm = document.getElementById("codm").value
     editedModelo.capacidade = document.getElementById("capacidade").value
     editedModelo.peso = document.getElementById("peso").value
     editedModelo.limite = document.getElementById("limite").value

     tempModeloList[updateIndex] = editedModelo
     
     localStorage.setItem("modelos", JSON.stringify(tempModeloList))
     
}

function saveUpdateSindicato(urlGuid){
     var url = new URLSearchParams(location.search)
     var urlGuid = url.get("id")
     
     var updateIndex = tempUserList.findIndex(sindicato => sindicato.id == urlGuid)
     var editedSindicato = tempSindicatoList[updateIndex]
     console.log(editedSindicato)
     
     editedSindicato.passport = document.getElementById("coda").value
     editedSindicato.coda = document.getElementById("codm").value

     tempSindicatoList[updateIndex] = editedSindicato
     
     localStorage.setItem("sindicato", JSON.stringify(tempSindicatoList))
     
}

function saveUpdateTecnico(urlGuid){
     var url = new URLSearchParams(location.search)
     var urlGuid = url.get("id")
     
     var updateIndex = tempTecnicoList.findIndex(users => users.id == urlGuid)
     var editedTecnico = tempTecnicoList[updateIndex]
     console.log(editedTenico)
     
     editedTecnico.nome = document.getElementById("nome").value
     editedTecnico.matricula = document.getElementById("matricula").value
     editedTecnico.nromembro = document.getElementById("nromembro").value
     editedTecnico.codm = document.getElementById("coda").value
     editedTecnico.cods = document.getElementById("cods").value
     editedTecnico.endereco = document.getElementById("endereco").value
     editedTecnico.telefone = document.getElementById("telefone").value
     editedTecnico.salario = document.getElementById("salario").value

     tempTecnicoList[updateIndex] = editedTecnico
     
     localStorage.setItem("tecnico", JSON.stringify(tempTecnicoList))
     
}

function saveUpdateTeste(urlGuid){
     var url = new URLSearchParams(location.search)
     var urlGuid = url.get("id")
     
     var updateIndex = tempTesteList.findIndex(users => users.id == urlGuid)
     var editedTeste = tempTesteList[updateIndex]
     console.log(editedTeste)
     
     editedTeste.codt = document.getElementById("codt").value
     editedTeste.codm = document.getElementById("codm").value
     editedTeste.hora = document.getElementById("hora").value
     editedTeste.pontuacao = document.getElementById("pontuacao").value
     editedTeste.data = document.getElementById("day").value + "/" + document.getElementById("month").value + "/" + document.getElementById("year").value

     tempTesteList[updateIndex] = editedTeste
     
     localStorage.setItem("teste", JSON.stringify(tempTesteList))
     
}

//----------------------------------------------
//----------------------------------------------

function getGUID(userObject, tableIndex){
     return getId = userObject[tableIndex].id
}

//----------------------------------------------

if (location.search != ''){
     getExistentInfo()
}
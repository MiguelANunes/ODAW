/*

    TABELA A SER INSERIDA, EDITADA E/OU EXCLUÍDA

*/

const tableBody = document.getElementById('tableBody');

async function deleteRow(idRow){
    await controladorService.delete(idRow)
        .then(res => res)
        .catch(rej => rej)
    tableFill()
}

async function updateRow(idRow) {
    if (window.confirm("Quer mesmo editar essa entrada?")) {
        window.location.href = `adicionar-controlador.html?guid=${idRow}`
    }
}

async function tableFill(){
    allControladores = await controladorService.listAll() // await = força a função async a esperar dar o return na promise
        .then(res => res.json())
        .catch(rej => console.log(rej));
    console.log(allControladores);
    let controladorInfo = '';
    allControladores.map(controlador => {
        newId = controlador.id
        controladorInfo += `
        <tr>
            <td class="col">${allControladores.indexOf(controlador)+1}</td>
            <td class="col">${controlador.matricula}</td>
            <td class="col">${controlador.nromembro}</td>
            <td class="col">${controlador.cods}</td>
            <td class="col">${controlador.data}</td>
            <td class="col">${controlador.nome}</td>
            <td class="col">
                <button class="action"><i class="bi bi-gear-fill cog" onclick = "updateRow('${controlador.id}')"></i></button>
                <button class="action"><i class="bi bi-x-circle-fill redX" onclick = "deleteRow('${controlador.id}')"></i></button>
            </td>
        </tr>
        `;
    });
    
    tableBody.innerHTML = controladorInfo;
}
/*

    TABELA A SER INSERIDA, EDITADA E/OU EXCLUÍDA

*/

const tableBody = document.getElementById('tableBody');

async function deleteRow(idRow){
    await sindicatoService.delete(idRow)
        .then(res => res)
        .catch(rej => rej)
    tableFill()
}

async function updateRow(idRow) {
    if (window.confirm("Quer mesmo editar essa entrada?")) {
        window.location.href = `adicionar-sindicato.html?guid=${idRow}`
    }
}

async function tableFill(){
    allSindicatos = await sindicatoService.listAll() // await = força a função async a esperar dar o return na promise
        .then(res => res.json())
        .catch(rej => console.log(rej));
    console.log(allSindicatos);
    let sindicatoInfo = '';
    allSindicatos.map(sindicato => {
        newId = sindicato.id
        sindicatoInfo += `
        <tr>
            <td class="col">${allSindicatos.indexOf(sindicato)+1}</td>
            <td class="col">${sindicato.cods}</td>
            <td class="col">${sindicato.nome}</td>
            <td class="col">
                <button class="action"><i class="bi bi-gear-fill cog" onclick = "updateRow('${sindicato.id}')"></i></button>
                <button class="action"><i class="bi bi-x-circle-fill redX" onclick = "deleteRow('${sindicato.id}')"></i></button>
            </td>
        </tr>
        `;
    });
    
    tableBody.innerHTML = sindicatoInfo;
}
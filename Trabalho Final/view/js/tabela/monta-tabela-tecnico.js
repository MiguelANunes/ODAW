/*

    TABELA A SER INSERIDA, EDITADA E/OU EXCLUÍDA

*/

const tableBody = document.getElementById('tableBody');

async function deleteRow(idRow){
    await tecnicoService.delete(idRow)
        .then(res => res)
        .catch(rej => rej)
    tableFill()
}

async function updateRow(idRow) {
    if (window.confirm("Quer mesmo editar essa entrada?")) {
        window.location.href = `adicionar-tecnico.html?guid=${idRow}`
    }
}

async function tableFill(){
    allTecnicos = await tecnicoService.listAll() // await = força a função async a esperar dar o return na promise
        .then(res => res.json())
        .catch(rej => console.log(rej));
    console.log(allTecnicos);
    let tecnicoInfo = '';
    allTecnicos.map(tecnico => {
        newId = tecnico.id
        tecnicoInfo += `
        <tr>
            <td class="col">${allTecnicos.indexOf(tecnico)+1}</td>
            <td class="col">${tecnico.matricula}</td>
            <td class="col">${tecnico.nromembro}</td>
            <td class="col">${tecnico.codm}</td>
            <td class="col">${tecnico.cods}</td>
            <td class="col">${tecnico.endereco}</td>
            <td class="col">${tecnico.telefone}</td>
            <td class="col">${tecnico.salario}</td>
            <td class="col">${tecnico.nome}</td>
            <td class="col">
                <button class="action"><i class="bi bi-gear-fill cog" onclick = "updateRow('${tecnico.id}')"></i></button>
                <button class="action"><i class="bi bi-x-circle-fill redX" onclick = "deleteRow('${tecnico.id}')"></i></button>
            </td>
        </tr>
        `;
    });
    
    tableBody.innerHTML = tecnicoInfo;
}
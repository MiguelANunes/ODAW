/*

    TABELA A SER INSERIDA, EDITADA E/OU EXCLUÍDA

*/

const tableBody = document.getElementById('tableBody');

async function deleteRow(idRow){
    await modeloService.delete(idRow)
        .then(res => res)
        .catch(rej => rej)
    tableFill()
}

async function updateRow(idRow) {
    if (window.confirm("Quer mesmo editar essa entrada?")) {
        window.location.href = `adicionar-modelo.html?guid=${idRow}`
    }
}

async function tableFill(){
    allModelos = await modeloService.listAll() // await = força a função async a esperar dar o return na promise
        .then(res => res.json())
        .catch(rej => console.log(rej));
    console.log(allModelos);
    let modeloInfo = '';
    allModelos.map(modelo => {
        newId = modelo.id
        modeloInfo += `
        <tr>
            <td class="col">${allModelos.indexOf(modelo)+1}</td>
            <td class="col">${modelo.codm}</td>
            <td class="col">${modelo.nome}</td>
            <td class="col">${modelo.capacidade}</td>
            <td class="col">${modelo.peso}</td>
            <td class="col">${modelo.limite}</td>
            <td class="col">
                <button class="action"><i class="bi bi-gear-fill cog" onclick = "updateRow('${modelo.id}')"></i></button>
                <button class="action"><i class="bi bi-x-circle-fill redX" onclick = "deleteRow('${modelo.id}')"></i></button>
            </td>
        </tr>
        `;
    });
    
    tableBody.innerHTML = modeloInfo;
}
/*

    TABELA A SER INSERIDA, EDITADA E/OU EXCLUÍDA

*/

const tableBody = document.getElementById('tableBody');

async function deleteRow(idRow){
    await testeService.delete(idRow)
        .then(res => res)
        .catch(rej => rej)
    tableFill()
}

async function updateRow(idRow) {
    if (window.confirm("Quer mesmo editar essa entrada?")) {
        window.location.href = `adicionar-teste.html?guid=${idRow}`
    }
}

async function tableFill(){
    allTestes = await testeService.listAll() // await = força a função async a esperar dar o return na promise
        .then(res => res.json())
        .catch(rej => console.log(rej));
    console.log(allTestes);
    let testeInfo = '';
    allTestes.map(teste => {
        newId = teste.id
        testeInfo += `
        <tr>
            <td class="col">${allTestes.indexOf(teste)+1}</td>
            <td class="col">${teste.codt}</td>
            <td class="col">${teste.codm}</td>
            <td class="col">${teste.data}</td>
            <td class="col">${teste.hora}</td>
            <td class="col">${teste.pontuacao}</td>
            <td class="col">
                <button class="action"><i class="bi bi-gear-fill cog" onclick = "updateRow('${teste.id}')"></i></button>
                <button class="action"><i class="bi bi-x-circle-fill redX" onclick = "deleteRow('${teste.id}')"></i></button>
            </td>
        </tr>
        `;
    });
    
    tableBody.innerHTML = testeInfo;
}
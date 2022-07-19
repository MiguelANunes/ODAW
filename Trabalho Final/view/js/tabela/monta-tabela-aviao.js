/*

    TABELA A SER INSERIDA, EDITADA E/OU EXCLUÍDA

*/

const tableBody = document.getElementById('tableBody');

async function deleteRow(idRow){
    await aviaoService.delete(idRow)
        .then(res => res)
        .catch(rej => rej)
    tableFill()
}

async function updateRow(idRow) {
    if (window.confirm("Quer mesmo editar essa entrada?")) {
        window.location.href = `adicionar-aviao.html?guid=${idRow}`
    }
}

async function tableFill(){
    allAviaos = await aviaoService.listAll() // await = força a função async a esperar dar o return na promise
        .then(res => res.json())
        .catch(rej => console.log(rej));
    console.log(allAviaos);
    let aviaoInfo = '';
    allAviaos.map(aviao => {
        newId = aviao.id
        aviaoInfo += `
        <tr>
            <td class="col">${allAviaos.indexOf(aviao)+1}</td>
            <td class="col">${aviao.coda}</td>
            <td class="col">${aviao.codm}</td>
            <td class="col">
                <button class="action"><i class="bi bi-gear-fill cog" onclick = "updateRow('${aviao.id}')"></i></button>
                <button class="action"><i class="bi bi-x-circle-fill redX" onclick = "deleteRow('${aviao.id}')"></i></button>
            </td>
        </tr>
        `;
    });
    
    tableBody.innerHTML = aviaoInfo;
}
myurl = 'https://localhost:5001/api/Crud/'

const controladorService =
{

    //GET BY ID
    searchById(rowInfo) {

        const tempControladorList = (res, rej) => {
            fetch(myurl+`${rowInfo}`, {
            method:'GET',
            headers:{
                'Content-Type':'application/json'
            },
        })
            .then(res)
            .catch(rej)
        }

        return new Promise(tempControladorList)
    },

    // GET ALL
    listAll() {
        const tempControladorList = (res, rej) => {
            fetch(myurl, {
            method:'GET',
            headers:{
                'Content-Type':'application/json'
            },
        })
            .then(res)
            .catch(rej)
        }

        return new Promise(tempControladorList)

    },

    // POST
    add() {
        var controlador = {
            id: this.generateGUID(),
            matricula: matricula.value,
            nromembro: nromembro.value,
            cods: cods.value,
            data: day.value + "/" + month.value + "/" + year.value,
            nome: nome.value
        }

        const tempControladorList = (res, rej) => {
            fetch(myurl, {
            method:'POST',
            headers:{
                'Content-Type':'application/json'
            },
            body: JSON.stringify(controlador)
        })
            .then(res)
            .catch(rej)
        }
        
        return new Promise(tempControladorList)
    },

    // PUT
    update(rowInfo) {
    var controlador = {
        matricula: matricula.value,
        nromembro: nromembro.value,
        cods: cods.value,
        data: day.value + "/" + month.value + "/" + year.value,
        nome: nome.value
    }

    fetch(myurl+`${rowInfo}`, {
        method:'PUT',
        headers:{
            'Content-Type':'application/json'
        },
        body: JSON.stringify(controlador)
    })
        .then(res => res)
        .catch(error => console.log(error))

    return new Promise(tempControladorList)
    },

    // DELETE
    delete(rowInfo) {
        
        if (window.confirm("Quer mesmo excluir essa entrada?")) {
            const tempControladorList = (res, rej) => {
                fetch(myurl+`${rowInfo}`, {
                method:'DELETE',
                headers:{
                    'Content-Type':'application/json'
                },
            })
                .then(res)
                .catch(rej)
            }
    
            return new Promise(tempControladorList)
        }
    },

    // GERAR UM ID PRA CADA PARTE DA TABELA SER ÚNICA
    generateGUID() {

        return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
            var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
            return v.toString(16);
        });
    }

}
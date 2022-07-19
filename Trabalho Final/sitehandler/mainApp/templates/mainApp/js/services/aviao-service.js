myurl = 'https://localhost:5001/api/Crud/'

const aviaoService =
{

    //GET BY ID
    searchById(rowInfo) {

        const tempAviaoList = (res, rej) => {
            fetch(myurl+`${rowInfo}`, {
            method:'GET',
            headers:{
                'Content-Type':'application/json'
            },
        })
            .then(res)
            .catch(rej)
        }

        return new Promise(tempAviaoList)
    },

    // GET ALL
    listAll() {
        const tempAviaoList = (res, rej) => {
            fetch(myurl, {
            method:'GET',
            headers:{
                'Content-Type':'application/json'
            },
        })
            .then(res)
            .catch(rej)
        }

        return new Promise(tempAviaoList)

    },

    // POST
    add() {
        var aviaos = {
            id: this.generateGUID(),
            coda: coda.value,
            codm: codm.value
        }

        const tempAviaoList = (res, rej) => {
            fetch(myurl, {
            method:'POST',
            headers:{
                'Content-Type':'application/json'
            },
            body: JSON.stringify(aviaos)
        })
            .then(res)
            .catch(rej)
        }
        
        return new Promise(tempAviaoList)
    },

    // PUT
    update(rowInfo) {
        var aviao = {
            coda: coda.value,
            codm: codm.value
        }

        fetch(myurl+`${rowInfo}`, {
            method:'PUT',
            headers:{
                'Content-Type':'application/json'
            },
            body: JSON.stringify(aviao)
        })
            .then(res => res)
            .catch(error => console.log(error))

    return new Promise(tempAviaoList)
    },

    // DELETE
    delete(rowInfo) {
        
        if (window.confirm("Quer mesmo excluir essa entrada?")) {
            const tempAviaoList = (res, rej) => {
                fetch(myurl+`${rowInfo}`, {
                method:'DELETE',
                headers:{
                    'Content-Type':'application/json'
                },
            })
                .then(res)
                .catch(rej)
            }
    
            return new Promise(tempAviaoList)
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
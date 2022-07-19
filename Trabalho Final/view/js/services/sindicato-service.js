myurl = 'https://localhost:5001/api/Crud/'

const sindicatoService =
{

    //GET BY ID
    searchById(rowInfo) {

        const tempSindicatoList = (res, rej) => {
            fetch(myurl+`${rowInfo}`, {
            method:'GET',
            headers:{
                'Content-Type':'application/json'
            },
        })
            .then(res)
            .catch(rej)
        }

        return new Promise(tempSindicatoList)
    },

    // GET ALL
    listAll() {
        const tempSindicatoList = (res, rej) => {
            fetch(myurl, {
            method:'GET',
            headers:{
                'Content-Type':'application/json'
            },
        })
            .then(res)
            .catch(rej)
        }

        return new Promise(tempSindicatoList)

    },

    // POST
    add() {
        var sindicato = {
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
            body: JSON.stringify(sindicato)
        })
            .then(res)
            .catch(rej)
        }
        
        return new Promise(tempAviaoList)
    },

    // PUT
    update(rowInfo) {
       var sindicato = {
            coda: coda.value,
            codm: codm.value
       }
       fetch(myurl+`${rowInfo}`, {
           method:'PUT',
           headers:{
               'Content-Type':'application/json'
           },
           body: JSON.stringify(sindicato)
       })
           .then(res => res)
           .catch(error => console.log(error))
    
       return new Promise(tempSindicatoList)
    },

    // DELETE
    delete(rowInfo) {
        
        if (window.confirm("Quer mesmo excluir essa entrada?")) {
            const tempSindicatoList = (res, rej) => {
                fetch(myurl+`${rowInfo}`, {
                method:'DELETE',
                headers:{
                    'Content-Type':'application/json'
                },
            })
                .then(res)
                .catch(rej)
            }
    
            return new Promise(tempSindicatoList)
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
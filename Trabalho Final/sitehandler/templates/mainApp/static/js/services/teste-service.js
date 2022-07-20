myurl = 'https://localhost:5001/api/Crud/'

const testeService =
{

    //GET BY ID
    searchById(rowInfo) {

        const tempTesteList = (res, rej) => {
            fetch(myurl+`${rowInfo}`, {
            method:'GET',
            headers:{
                'Content-Type':'application/json'
            },
        })
            .then(res)
            .catch(rej)
        }

        return new Promise(tempTesteList)
    },

    // GET ALL
    listAll() {
        const tempTesteList = (res, rej) => {
            fetch(myurl, {
            method:'GET',
            headers:{
                'Content-Type':'application/json'
            },
        })
            .then(res)
            .catch(rej)
        }

        return new Promise(tempTesteList)

    },

    // POST
    add() {
        var teste = {
            id: this.generateGUID(),
            codt: codt.value,
            codm: codm.value,
            data: day.value + "/" + month.value + "/" + year.value,
            hora: hora.value,
            pontuacao: pontuacao.value
        }

        const tempTesteList = (res, rej) => {
            fetch(myurl, {
            method:'POST',
            headers:{
                'Content-Type':'application/json'
            },
            body: JSON.stringify(teste)
        })
            .then(res)
            .catch(rej)
        }
        
        return new Promise(tempTesteList)
    },

    // PUT
    update(rowInfo) {
            
            var teste = {
                codt: codt.value,
                codm: codm.value,
                data: day.value + "/" + month.value + "/" + year.value,
                hora: hora.value,
                pontuacao: pontuacao.value
            }
    
            fetch(myurl+`${rowInfo}`, {
                method:'PUT',
                headers:{
                    'Content-Type':'application/json'
                },
                body: JSON.stringify(teste)
            })
                .then(res => res)
                .catch(error => console.log(error))

            return new Promise(tempTesteList)
    },

    // DELETE
    delete(rowInfo) {
        
        if (window.confirm("Quer mesmo excluir essa entrada?")) {
            const tempTesteList = (res, rej) => {
                fetch(myurl+`${rowInfo}`, {
                method:'DELETE',
                headers:{
                    'Content-Type':'application/json'
                },
            })
                .then(res)
                .catch(rej)
            }
    
            return new Promise(tempTesteList)
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
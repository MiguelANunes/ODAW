myurl = 'https://localhost:5001/api/Crud/'

const modeloService =
{

    //GET BY ID
    searchById(rowInfo) {

        const tempModeloList = (res, rej) => {
            fetch(myurl+`${rowInfo}`, {
            method:'GET',
            headers:{
                'Content-Type':'application/json'
            },
        })
            .then(res)
            .catch(rej)
        }

        return new Promise(tempModeloList)
    },

    // GET ALL
    listAll() {
        const tempModeloList = (res, rej) => {
            fetch(myurl, {
            method:'GET',
            headers:{
                'Content-Type':'application/json'
            },
        })
            .then(res)
            .catch(rej)
        }

        return new Promise(tempModeloList)

    },

    // POST
    addModelos() {
        var modelos = {
            id: this.generateGUID(),
            codm: codm.value,
            nome: nome.value,
            capacidade: capacidade.value,
            peso: peso.value,
            limite: limite.value
        }

        const tempModeloList = (res, rej) => {
            fetch(myurl, {
            method:'POST',
            headers:{
                'Content-Type':'application/json'
            },
            body: JSON.stringify(modelos)
        })
            .then(res)
            .catch(rej)
        }
        
        return new Promise(tempModeloList)
    },

    // PUT
    update(rowInfo) {
            
            var modelo = {
                codm: codm.value,
                nome: nome.value,
                capacidade: capacidade.value,
                peso: peso.value,
                limite: limite.value
            }
    
            fetch(myurl+`${rowInfo}`, {
                method:'PUT',
                headers:{
                    'Content-Type':'application/json'
                },
                body: JSON.stringify(modelo)
            })
                .then(res => res)
                .catch(error => console.log(error))

            return new Promise(tempModeloList)
    },

    // DELETE
    delete(rowInfo) {
        
        if (window.confirm("Quer mesmo excluir essa entrada?")) {
            const tempModeloList = (res, rej) => {
                fetch(myurl+`${rowInfo}`, {
                method:'DELETE',
                headers:{
                    'Content-Type':'application/json'
                },
            })
                .then(res)
                .catch(rej)
            }
    
            return new Promise(tempModeloList)
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
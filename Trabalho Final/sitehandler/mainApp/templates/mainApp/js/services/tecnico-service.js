myurl = 'https://localhost:5001/api/Crud/'

const tecnicoService =
{

    //GET BY ID
    searchById(rowInfo) {

        const tempTecnicoList = (res, rej) => {
            fetch(myurl+`${rowInfo}`, {
            method:'GET',
            headers:{
                'Content-Type':'application/json'
            },
        })
            .then(res)
            .catch(rej)
        }

        return new Promise(tempTecnicoList)
    },

    // GET ALL
    listAll() {
        const tempTecnicoList = (res, rej) => {
            fetch(myurl, {
            method:'GET',
            headers:{
                'Content-Type':'application/json'
            },
        })
            .then(res)
            .catch(rej)
        }

        return new Promise(tempTecnicoList)

    },

    // POST
    add() {
        var tecnico = {
            id: this.generateGUID(),
            matricula: codm.value,
            nromembro: nromembro.value,
            codm: codm.value,
            cods: cods.value,
            endereco: endereco.value,
            telefone: telefone.value,
            salario: salario.value,
            nome:nome.value,
        }

        const tempTecnicoList = (res, rej) => {
            fetch(myurl, {
            method:'POST',
            headers:{
                'Content-Type':'application/json'
            },
            body: JSON.stringify(tecnico)
        })
            .then(res)
            .catch(rej)
        }
        
        return new Promise(tempTecnicoList)
    },

    // PUT
    update(rowInfo) {
            
            var tecnico = {
                matricula: codm.value,
                nromembro: nromembro.value,
                codm: codm.value,
                cods: cods.value,
                endereco: endereco.value,
                telefone: telefone.value,
                salario: salario.value,
                nome:nome.value,
            }
    
            fetch(myurl+`${rowInfo}`, {
                method:'PUT',
                headers:{
                    'Content-Type':'application/json'
                },
                body: JSON.stringify(tecnico)
            })
                .then(res => res)
                .catch(error => console.log(error))

            return new Promise(tempTecnicoList)
    },

    // DELETE
    delete(rowInfo) {
        
        if (window.confirm("Quer mesmo excluir essa entrada?")) {
            const tempTecnicoList = (res, rej) => {
                fetch(myurl+`${rowInfo}`, {
                method:'DELETE',
                headers:{
                    'Content-Type':'application/json'
                },
            })
                .then(res)
                .catch(rej)
            }
    
            return new Promise(tempTecnicoList)
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
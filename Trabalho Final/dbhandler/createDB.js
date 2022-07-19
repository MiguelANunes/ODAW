db = connect( 'mongodb://localhost/Aeroporto' );
db.avioes.insertMany( 
   [
      {
         coda: 1,
         codm: 2,
         pontuacao: 0
      },
      {
         coda: 2,
         codm: 1,
         pontuacao: 95
      },
      {
         coda: 3,
         codm: 1,
         pontuacao: 90
      },
      {
         coda: 4,
         codm: 1,
         pontuacao: 92
      },
      {
         coda: 5,
         codm: 4,
         pontuacao: 100
      },
      {
         coda: 6,
         codm: 4,
         pontuacao: 100
      },
      {
         coda: 7,
         codm: 5,
         pontuacao: 85
      },
      {
         coda: 8,
         codm: 6,
         pontuacao: 50
      },
      {
         coda: 9,
         codm: 3,
         pontuacao: 89
      },
      {
         coda: 10,
         codm: 1,
         pontuacao: 78
      },
      {
         coda: 11,
         codm: 3,
         pontuacao: 95
      }
   ] 
)

db.modelos.insertMany(
   [
      {
         codm: 1,
         nome: "Boeing 767",
         capacidade: 200,
         peso: 80500,
         limite: 3,
         avioes: [2, 3, 4, 10]
      },
      {
         codm: 2,
         nome: "An-225",
         capacidade: 300,
         peso: 100000,
         limite: 1,
         avioes: [1]
      },
      {
         codm: 3,
         nome: "Boeing 777",
         capacidade: 250,
         peso: 80250,
         limite: 2,
         avioes: [11, 9]
      },
      {
         codm: 4,
         nome: "EMB-314",
         capacidade: 2,
         peso: 3200,
         limite: 5,
         avioes: [5, 6]
      },
      {
         codm: 5,
         nome: "F-16",
         capacidade: 2,
         peso: 9100,
         limite: 6,
         avioes: [7]
      },
      {
         codm: 6,
         nome: "Ju-87",
         capacidade: 2,
         peso: 4000,
         limite: 2,
         avioes: [8]
      }
   ]   
)

db.controladores.insertMany(
   [
      {
         matricula: 1,
         nroMembro: 100,
         cods: 2,
         dataExame: new Date(2022,04,14),
         nome: "Miguel"
      },
      {
         matricula: 2,
         nroMembro: 200,
         cods: 2,
         dataExame: new Date(2021,10,20),
         nome: "Daniella"
      },
      {
         matricula: 3,
         nroMembro: 150,
         cods: 2,
         dataExame: new Date(2022,00,03),
         nome: "Eduardo"
      },
      {
         matricula: 4,
         nroMembro: 999,
         cods: 2,
         dataExame: new Date(2019,03,12),
         nome: "Rodrigo"
      }
   ]
)

 db.sindicatos.insertMany(
   [
      {
         nome: "SINDTECNICOS",
         cods: 1,
         tecnicos: [1, 2, 3]
      },
      {
         nome: "SINDCONTROLADOR",
         cods: 2,
         controladores: [1, 2, 3, 4]
      }
   ]
)

db.testes.insertMany(
   [
      {
         codt: 1,
         coda: 1,
         data: new Date(2019,07,14),
         duracao: 2,
         pontuacaoMax: 100
      },
      {
         codt: 2,
         coda: 8,
         data: new Date(1944,09,03),
         duracao: 4,
         pontuacaoMax: 100
      },
      {
         codt: 3,
         coda: 5,
         data: new Date(1993,01,11),
         duracao: 5,
         pontuacaoMax: 100
      },
      {
         codt: 4,
         coda: 5,
         data: new Date(1994,10,20),
         duracao: 4,
         pontuacaoMax: 100
      },
      {
         codt: 5,
         coda: 7,
         data: new Date(2003,03,28),
         duracao: 8,
         pontuacaoMax: 100
      },
      {
         codt: 6,
         coda: 9,
         data: new Date(2014-03-01),
         duracao: 12,
         pontuacaoMax: 100
      }
   ]
)

db.tecnicos.insertMany(
   [
      {
         matricula: 1,
         nroMembro: 250,
         cods: 1,
         codm: 1,
         endereco: "Joinville",
         telefone: "91234-5678",
         salario: 4000.00,
         nome: "Thiago"
      },
      {
         matricula: 2,
         nroMembro: 300,
         cods: 3,
         codm: 1,
         endereco: "Araquari",
         telefone: "91237-9856",
         salario: 6500.00,
         nome: "Gilson"
      },
      {
         matricula: 3,
         nroMembro: 375,
         cods: 5,
         codm: 1,
         endereco: "Joinville",
         telefone: "95678-1234",
         salario: 2300.00,
         nome: "Danilo"
      }
   ]
)
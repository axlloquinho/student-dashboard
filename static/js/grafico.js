let bimestre_atual;
var materias = ['geografia','projeto de vida', 'Física', 'Matemática', 'ingles', 'português','Ciência' ,'Educação física', 'Sociologia']
let tipo_grafico;

const cores = materias.map(() => corAleatoria());

let notas_bimestre = {
  "1": [4, 2, 7, 6, 6, 7, 8, 5],
  "2": [6, 0, 1, 5, 8, 9, 6, 0],
  "3": [2, 8, 5, 9, 3, 3, 2, 7],
  "4": [0, 1, 4, 9, 7, 2, 9, 1]
}

function corAleatoria() {
  const r = Math.floor(Math.random() * 156) + 100;
  const g = Math.floor(Math.random() * 156) + 100;
  const b = Math.floor(Math.random() * 156) + 100;
  
  return `rgb(${r}, ${g}, ${b})`;
}

let notas = notas_bimestre[1]

const ctx = document.getElementById("grafico_notas").getContext('2d')

let grafico = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: materias,
    datasets: [{
      data: notas,
      label: "primeiro bimestre",
      backgroundColor: cores
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false
  }
})

// atualizar gráfico
function atualizarGrafico() {
  const tipo = document.getElementById('tipos_graficos').value
  const bimestre = document.getElementById('bimestre').value
  
  const notas = notas_bimestre[bimestre]
  
  grafico.destroy()
  
  grafico = new Chart(ctx, {
    type: tipo,
    data: {
      labels: materias,
      datasets: [{
        data: notas,
        label: bimestre + "° bimestre",
        backgroundColor: cores
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false
    }
  })
}

// legenda
let legenda = document.getElementById("legenda");

materias.forEach((materia, i) => {
  let item = document.createElement("div");
  
  item.innerHTML = `
    <span style="
      display:inline-block;
      width:15px;
      height:15px;
      background:${cores[i]};
      margin-right:8px;
    "></span>
    ${materia}
  `;
  
  legenda.appendChild(item);
});
// Exemplo de dados estáticos (mock) para o gráfico de faturamento
var options = {
    chart: {
    type: 'area',
    height: 260,
    toolbar: { show: false },
    fontFamily: 'inherit',
    },
    colors: ['#6366f1'],
    dataLabels: { enabled: false },
    stroke: { curve: 'smooth', width: 3 },
    series: [{
    name: 'Faturamento (R$)',
    data: [12000, 15000, 11000, 18000, 17000, 21000, 19500, 22000, 20500, 23000, 25000, 24000]
    }],
    xaxis: {
    categories: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
    labels: { style: { colors: '#6b7280' } }
    },
    yaxis: {
    labels: { style: { colors: '#6b7280' } }
    },
    fill: {
    type: 'gradient',
    gradient: {
        shadeIntensity: 1,
        opacityFrom: 0.4,
        opacityTo: 0.1,
        stops: [0, 90, 100]
    }
    },
    grid: { borderColor: '#e5e7eb', strokeDashArray: 4 },
    tooltip: {
    y: {
        formatter: function (val) { return 'R$ ' + val.toLocaleString('pt-BR'); }
    }
    }
};



document.addEventListener('DOMContentLoaded', function () {
    if (document.querySelector("#faturamentoApexChart")) {
        var chart = new ApexCharts(document.querySelector("#faturamentoApexChart"), options);
        chart.render();
    }
});
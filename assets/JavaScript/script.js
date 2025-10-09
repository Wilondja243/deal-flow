
const DEFAULT_COLORS = [
    'rgba(255, 99, 132, 0.7)',
    'rgba(54, 162, 235, 0.7)',
    'rgba(255, 206, 86, 0.7)',
    'rgba(75, 192, 192, 0.7)'
]


function chart(type, label_data, data, label='', canvasElement){

    if(canvasElement){
        const ctx = canvasElement.getContext('2d');

        new Chart(ctx, {
            type: type,
            data: {
                labels: label_data,
                datasets: [{
                    label: label,
                    data: data,
                    backgroundColor: (type === 'bar') ? DEFAULT_COLORS[1] : DEFAULT_COLORS,
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,

                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        })
    }
}


document.addEventListener('DOMContentLoaded', function() {

    const canvasElement = document.getElementById('pipelineChart');
    const canvasElement2 = document.getElementById('activityChart');

    if(canvasElement){
        chart(
            'bar',
            ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Séptembre', 'Octobre', 'Novembre', 'Décembre'],
            [12000, 19000, 3000, 5000,12000, 19000, 3000, 5000, 12000, 19000, 3000, 5000],
            'Activités ',
            canvasElement
        )

    }

    if(canvasElement2){
        chart(
            'doughnut',
            ['Qualification', 'Proposition', 'Négociation', 'Gagnée'],
            [12000, 19000, 3000, 5000],
            'Valeur du Pipeline (€)',
            canvasElement2
        )
    }

});

document.addEventListener('DOMContentLoaded', function() {
    const canvasElement = document.getElementById('pipelineChart');

    const ctx = canvasElement.getContext('2d');

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Qualification', 'Proposition', 'Négociation', 'Gagnée'],
            datasets: [{
                label: 'Valeur du Pipeline (€)',
                data: [12000, 19000, 3000, 5000],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.7)',
                    'rgba(54, 162, 235, 0.7)',
                    'rgba(255, 206, 86, 0.7)',
                    'rgba(75, 192, 192, 0.7)'
                ]
            }]
        },
        options: {
            // Options pour rendre le graphique responsive, etc.
        }
    });
});
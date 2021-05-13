document.addEventListener('DOMContentLoaded', function () {
    const total_stats = document.getElementById('total-stats')
    
    var hp = document.getElementById('hp').innerHTML
    var attack = document.getElementById('attack').innerHTML
    var defense = document.getElementById('defense').innerHTML
    var special_attack = document.getElementById('special-attack').innerHTML
    var special_defense = document.getElementById('special-defense').innerHTML
    var speed = document.getElementById('speed').innerHTML

    var data = [hp, attack, defense, special_attack, special_defense, speed]

    let total = 0
    for (const value of data) {
        total += parseInt(value)
    }
    
    total_stats.innerHTML = `Total: ${total}`

    var ctx = document.getElementById('stats-chart').getContext('2d');
    var stats_chart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Hp', 'Atk', 'Def', 'Sp. Atk', 'Sp. Def', 'Spd'],
            datasets: [{
                label: 'Stat',
                data: data,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1.5
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    const base_pokemon = document.getElementById('base-pokemon')
    const first_stages = document.getElementById('first-stages')
    const second_stages = document.getElementById('second-stages')

    if (second_stages) {
        base_pokemon.classList.replace('w-100', 'w-33')
        first_stages.classList.add('w-33')
        second_stages.classList.add('w-33')
    } else if (first_stages) {
        base_pokemon.classList.replace('w-100', 'w-50')
        first_stages.classList.add('w-50')
    }
})
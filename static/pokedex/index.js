document.addEventListener('DOMContentLoaded', function () {
    const pokemon_form = document.getElementById('pokemon-search')
    const pokemon_query = document.getElementsByName('pokemon-query')[0]

    const move_form = document.getElementById('move-search')
    const move_query = document.getElementsByName('move-query')[0]

    const ability_form = document.getElementById('ability-search')
    const ability_query = document.getElementsByName('ability-query')[0]

    pokemon_form.onsubmit = event => {
        event.preventDefault()
        window.location.replace(`/pokemon/${pokemon_query.value.toLowerCase().replace(' ', '-').replace("'", '')}`)
    }

    move_form.onsubmit = event => {
        event.preventDefault()
        window.location.replace(`/move/${move_query.value.toLowerCase().replace(' ', '-').replace("'", '')}`)
    }

    ability_form.onsubmit = event => {
        event.preventDefault()
        window.location.replace(`/ability/${ability_query.value.toLowerCase().replace(' ', '-').replace("'", '')}`)
    }
})
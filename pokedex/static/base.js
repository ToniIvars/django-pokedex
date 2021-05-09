document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('search-form')
    const query = document.getElementsByName('query')[0]

    form.onsubmit = event => {
        event.preventDefault()
        window.location.replace(`/pokedex/pokemon/${query.value.toLowerCase()}`)
    }
})
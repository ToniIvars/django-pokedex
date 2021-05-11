document.addEventListener('DOMContentLoaded', function () {
    const gen_title = document.querySelector('#gen-title')
    const gen_buttons = Array.from(document.querySelectorAll('.gen-buttons'))
    const gen_tables = Array.from(document.querySelectorAll('.gen-tables'))

    const dropdown_buttons = Array.from(document.querySelectorAll('.dropdown-toggle'))

    gen_buttons.slice(-1).pop().classList.add('button-disabled')
    gen_buttons.slice(-1).pop().disabled = true
    document.getElementById(gen_buttons.slice(-1).pop().id.slice(4)).classList.remove('d-none')
    gen_title.innerHTML = 'Generation 7'

    gen_buttons.forEach(btn => {
        btn.onclick = () => {
            gen_buttons.forEach(element => {
                element.classList.remove('button-disabled')
                element.disabled = false
            })
            gen_tables.forEach(element => element.classList.add('d-none'))

            btn.classList.add('button-disabled')
            btn.disabled = true
            document.getElementById(btn.id.slice(4)).classList.remove('d-none')

            gen_title.innerHTML = `Generation ${btn.id.slice(-1)}`
        }
    })

    dropdown_buttons.forEach(btn => {
        btn.onclick = () => {
            const table_id = btn.id.split('-').slice(1).join('-')
            const table = document.getElementById(table_id)

            if (table.classList.contains('d-none')) {
                table.classList.remove('d-none')
            } else {
                table.classList.add('d-none')
            }
        }
    })
})
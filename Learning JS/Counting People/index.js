//document.getElementById("count").innerText = 15


let element_count = document.getElementById('count')
let element_entries = document.getElementById('entries')
let count = 0

function increment(){
    count += 1
    element_count.textContent = count
}

function save(){
        element_entries.textContent += count + ' - '
        count = 0
        element_count.textContent = count
}
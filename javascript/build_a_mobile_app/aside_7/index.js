const counterElement = document.getElementById("counter")
const clickElement = document.getElementById("click")

let counter = 0

clickElement.addEventListener("click", function() {
    counter++
    
    counterElement.textContent = counter
})

let countElement = document.getElementById("count-element")
let savedElement = document.getElementById("save-element")

let count = 0

function increment() {
	count += 1
	countElement.textContent = count
}

function save() {
	let countString = count + " - "
	savedElement.textContent += countString
	countElement.textContent = 0
	count = 0
}

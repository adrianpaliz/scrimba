let countElement = document.getElementById("count-element")
let savedElement = document.getElementById("save-element")

let count = 0

function increment() {
	count += 1
	countElement.innerText = count
}

function save() {
	let countString = count + " - "
	savedElement.innerText += countString

}

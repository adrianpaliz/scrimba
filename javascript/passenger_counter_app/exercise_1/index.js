let countElement = document.getElementById("count-element")

let count = 0

function increment() {
	count = count + 1
	countElement.innerText = count
}

function save() {
	console.log(count)
}

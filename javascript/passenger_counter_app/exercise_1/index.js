let countElement = document.getElementById("count-element")

let count = 0

function increment() {
	count += 1
	countElement.innerText = count
}

function save() {
	let savedElement = " " + count + " - "
	paragraphTag = document.getElementById("save-element")
	paragraphTag.innerText = paragraphTag.innerText + savedElement


	console.log(count)
}

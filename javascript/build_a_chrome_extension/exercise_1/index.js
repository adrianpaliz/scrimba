let myLeads =[]
const inputElement = document.getElementById("input-element")
const inputButtom = document.getElementById("input-button")
const unorderedListElement = document.getElementById("unordered-list-element")

inputButtom.addEventListener("click", function() {
	myLeads.push(inputElement.value)
	inputElement.value = ""
	renderLeads()
})

function renderLeads() {
	let listItems = ""
	for (let index = 0; index < myLeads.length; index++) {	
	listItems += "<li>" + myLeads[index] + "</li>"
	}
	unorderedListElement.innerHTML = listItems
}

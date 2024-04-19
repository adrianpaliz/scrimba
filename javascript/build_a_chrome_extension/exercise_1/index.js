let myLeads = []
const inputElement = document.getElementById("input-element")
const inputButton = document.getElementById("input-button")
const unorderedListElement = document.getElementById("unordered-list-element")
const deleteButton = document.getElementById("delete-button")
const leadsFromLocalStorage = JSON.parse( localStorage.getItem("myLeads") )

if (leadsFromLocalStorage) {
	myLeads = leadsFromLocalStorage 
	renderLeads()
}

deleteButton.addEventListener("dblclick", function() {
	localStorage.clear()
	myLeads = []
	renderLeads()
}) 

inputButton.addEventListener("click", function() {
	myLeads.push(inputElement.value)
	inputElement.value = ""
	localStorage.setItem("myLeads", JSON.stringify(myLeads) )
	renderLeads()	
})

function renderLeads() {
	let listItems = ""
	for (let index = 0; index < myLeads.length; index++) {
	 	listItems += `
			<li>
				<a target="_blank" href="${myLeads[index]}">
					${myLeads[index]}
				</a>
			</li>
		`
	}
	unorderedListElement.innerHTML = listItems
}

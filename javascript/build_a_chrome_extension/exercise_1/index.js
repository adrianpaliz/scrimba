let myLeads = []
let oldLeads = []
const inputElement = document.getElementById("input-element")
const inputButton = document.getElementById("input-button")
const unorderedListElement = document.getElementById("unordered-list-element")
const deleteButton = document.getElementById("delete-button")
const leadsFromLocalStorage = JSON.parse( localStorage.getItem("myLeads") )

if (leadsFromLocalStorage) {
	myLeads = leadsFromLocalStorage 
	render(myLeads)
}

function render(leads) {
	let listItems = ""
	for (let index = 0; index < leads.length; index++) {
	 	listItems += `
			<li>
				<a target="_blank" href="${leads[index]}">
					${leads[index]}
				</a>
			</li>
		`
	}
	unorderedListElement.innerHTML = listItems
}

deleteButton.addEventListener("dblclick", function() {
	localStorage.clear()
	myLeads = []
	render(myLeads)
}) 

inputButton.addEventListener("click", function() {
	myLeads.push(inputElement.value)
	inputElement.value = ""
	localStorage.setItem("myLeads", JSON.stringify(myLeads) )
	render(myLeads)	
})

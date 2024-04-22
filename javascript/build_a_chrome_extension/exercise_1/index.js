let myLeads = []
const inputElement = document.getElementById("input-element")
const inputButton = document.getElementById("input-button")
const unorderedListElement = document.getElementById("unordered-list-element")
const deleteButton = document.getElementById("delete-button")
const leadsFromLocalStorage = JSON.parse( localStorage.getItem("myLeads") )
const saveTabButton = document.getElementById("save-tab-button")

if (leadsFromLocalStorage) {
	myLeads = leadsFromLocalStorage 
	render(myLeads)
}

const tabs = [
	{url: "https://www.linkedin.com/in/adrianpaliz/"}
]

saveTabButton.addEventListener("click", function(){
	console.log(tabs[0].url)
})

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

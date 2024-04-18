let myLeads = []
const inputElement = document.getElementById("input-element")
const inputButtom = document.getElementById("input-button")
const unorderedListElement = document.getElementById("unordered-list-element")

let leadsFromLocalStorage = JSON.parse( localStorage.getItem("myLeads") )
console.log(leadsFromLocalStorage)

inputButtom.addEventListener("click", function() {
	myLeads.push(inputElement.value)
	inputElement.value = ""
	localStorage.setItem("myLeads", JSON.stringify(myLeads) )
	renderLeads()	

	console.log( localStorage.getItem("myLeads") )
})

function renderLeads() {
	let listItems = ""
	for (let index = 0; index < myLeads.length; index++) {
	 // listItems += "<li><a target='_blank' href='" + myLeads[index] + "'>" + myLeads[index] + "</a></li>"
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

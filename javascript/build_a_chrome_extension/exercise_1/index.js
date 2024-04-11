let myLeads =["www.awesomelead.com", "www.epiclead.com", "www.greatlead.com"]

const inputElement = document.getElementById("input-element")
const inputButtom = document.getElementById("input-button")
const unorderedListElement = document.getElementById("unordered-list-element")

inputButtom.addEventListener("click", function() {
	myLeads.push(inputElement.value)
	console.log(myLeads)
})

for (let index = 0; index < myLeads.length; index++) {	
	unorderedListElement.innerHTML += "<li>" + myLeads[index] + "</li>"
}

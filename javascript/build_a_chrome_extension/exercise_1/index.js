let myLeads =[]

const inputElement = document.getElementById("input-element")
const inputButtom = document.getElementById("input-button")

inputButtom.addEventListener("click", function() {
	myLeads.push("www.awesomelead.com")
	console.log(myLeads)
})

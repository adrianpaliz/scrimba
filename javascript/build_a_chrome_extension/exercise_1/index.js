let myLeads =["www.awesomelead.com", "www.epiclead.com", "www.greatlead.com"]

const inputElement = document.getElementById("input-element")
const inputButtom = document.getElementById("input-button")

inputButtom.addEventListener("click", function() {
	myLeads.push(inputElement.value)
	console.log(myLeads)
})

for (let index = 0; index < myLeads.length; index++) {	
	console.log(myLeads[index]) 
}

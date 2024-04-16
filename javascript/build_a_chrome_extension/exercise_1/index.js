let myLeads =[]
const inputElement = document.getElementById("input-element")
const inputButtom = document.getElementById("input-button")
const unorderedListElement = document.getElementById("unordered-list-element")

//localStorage.setItem("mySite", "www.baidu.com")
//localStorage.getItem("mySite")
//let domain = localStorage.getItem("mySite")
//console.log(domain)
//localStorage.clear()

inputButtom.addEventListener("click", function() {
	myLeads.push(inputElement.value)
	inputElement.value = ""
	renderLeads()
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

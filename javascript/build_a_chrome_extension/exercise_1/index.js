let myLeads = `["www.1337x.to"]`

// 1. Turn the myLeads string into a array
myLeads = JSON.parse(myLeads)
// 2 Push a new value to the string
myLeads.push("www.yts.mx")
// 3 Turn the array into a string again
myLeads = JSON.stringify(myLeads)
// 4 Console.log the string using typeof to verify that it's a string
console.log(typeof myLeads)


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

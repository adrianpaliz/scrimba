import { initializeApp } from "https://www.gstatic.com/firebasejs/10.11.1/firebase-app.js"
import { getDatabase, ref, push, onValue } from "https://www.gstatic.com/firebasejs/10.11.1/firebase-database.js"

const appSettings = {
	databaseURL: ""
}

const app = initializeApp(appSettings)
const database = getDatabase(app)
const shoppingListInDataBase = ref(database, "shoppingList")

const inputFieldElement = document.getElementById("input-field")
const addButtonElement = document.getElementById("add-button")
const shoppingListElement = document.getElementById("shopping-list")

addButtonElement.addEventListener("click", function(){
	let inputValue = inputFieldElement.value
	push(shoppingListInDataBase, inputValue)
	clearInputFieldElement()
})

onValue(shoppingListInDataBase, function(snapshot) {
	let itemsArray = Object.entries(snapshot.val())
	
	clearShoppingListElement()
	
	for (let index = 0; index < itemsArray.length; index++)	{
		let currentItem = itemsArray[index]
		let currentItemID = currentItem[0]
		let currentItemValue = currentItem[1]

		appendItemToShoppingListElement(currentItem)
	}
	
})
function clearShoppingListElement() {
	shoppingListElement.innerHTML = ""
}

function clearInputFieldElement() {
	inputFieldElement.value = ""		
}

function appendItemToShoppingListElement(item) {
	let itemID = item[0]
	let itemValue = item[1]
	
	let newElement = document.createElement("li")
	
	newElement.textContent = itemValue
	shoppingListElement.append(newElement)

}

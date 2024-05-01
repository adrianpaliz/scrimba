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
	appendItemToShoppingListElement(inputValue) 
})

onValue(shoppingListInDataBase, function(snapshot) {
	let itemsArray = Object.values(snapshot.val())
	
	for (let index = 0; index < itemsArray.length; index++)	{
		let currentItem = itemsArray[index]
		appendItemToShoppingListElement(currentItem)
	}

})

function clearInputFieldElement() {
	inputFieldElement.value = ""		
}

function appendItemToShoppingListElement(itemValue) {
	shoppingListElement.innerHTML += `<li>${itemValue}</li>`
}


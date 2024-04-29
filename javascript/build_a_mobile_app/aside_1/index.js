import { initializeApp } from "https://www.gstatic.com/firebasejs/10.11.1/firebase-app.js"
import { getDatabase, ref, push } from "https://www.gstatic.com/firebasejs/10.11.1/firebase-database.js"

const appSettings = {
    databaseURL: ""
}
const app = initializeApp(appSettings)
const database = getDatabase(app)
const moviesInDataBase = ref(database, "movies")

const inputFieldElement = document.getElementById("input-field")
const addButtonElement = document.getElementById("add-button")

addButtonElement.addEventListener("click", function(){
    let inputValue = inputFieldElement.value
	push(moviesInDataBase, inputValue)
    console.log(inputValue)
npm init})

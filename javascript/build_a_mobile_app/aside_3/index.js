import { initializeApp } from "https://www.gstatic.com/firebasejs/10.11.1/firebase-app.js"
import { getDatabase, ref, onValue } from "https://www.gstatic.com/firebasejs/10.11.1/firebase-database.js"

const appSettings = {
    databaseURL: ""
}

const app = initializeApp(appSettings)
const database = getDatabase(app)
const booksInDataBase = ref(database, "books")

const booksElement = document.getElementById("books")

onValue(booksInDataBase, function(snapshot) {
	let booksArray = Object.values(snapshot.val())
	clearBooksListElement()
	
	for (let index = 0; index < booksArray.length; index++ ) {
		let currentBook = booksArray[index]
		appendBookToBooksListElement(currentBook)
	}
})

function clearBooksListElement() {
    booksElement.innerHTML = ""
}

function appendBookToBooksListElement(bookValue) {
    booksElement.innerHTML += `<li>${bookValue}</li>`
}

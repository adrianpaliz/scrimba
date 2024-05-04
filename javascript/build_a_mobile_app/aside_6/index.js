import { initializeApp } from "https://www.gstatic.com/firebasejs/10.11.1/firebase-app.js"
import { getDatabase, ref, onValue } from "https://www.gstatic.com/firebasejs/10.11.1/firebase-database.js"

const appSettings = {
	databaseURL: ""
}

const app = initializeApp(appSettings)
const database = getDatabase(app)
const newsStoriesInDataBase = ref(database, "newsStories")

const storiesElement = document.getElementById("stories")

onValue(newsStoriesInDataBase, function(snapshot) {
	let newsStoriesArray = Object.entries(snapshot.val())
	
	storiesElement.innerHTML = ""

	for (let index = 0; index < newsStoriesArray.length; index++) {
		let currentStory = newsStoriesArray[index]

		appendStoryToStoriesElement(currentStory)
	}
})

function appendStoryToStoriesElement(story) {
	let storyID = story[0]
	let storyTitle = story[1]

	let newElement = document.createElement("div")
	
	newElement.classList.add("story")

	newElement.textContent = storyTitle

	newElement.addEventListener("dblclick", function() {

	})

	storiesElement.append(newElement)
}

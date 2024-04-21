const welcomeElement = document.getElementById("welcome-element")

function greetUser(greeting, name) {
	welcomeElement.textContent = greeting + ", " + name + "  👋"
}

greetUser("Alli puncha", "Adrián")


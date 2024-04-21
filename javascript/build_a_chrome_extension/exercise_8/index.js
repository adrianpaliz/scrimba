const welcomeElement = document.getElementById("welcome-element")

function greetUser(greeting, name, emoji) {
	welcomeElement.textContent = `${greeting}, ${name} ${emoji}`
}

greetUser("Alli puncha", "Adrián", "🤗")


let firstCard = 11 
let secondCard = 11

let sum = firstCard + secondCard

let hasBlackJack = false
let isAlive = true
let message = ""

let messageElement = document.getElementById("message-element")
let sumElement = document.getElementById("sum-element")

function startGame() {
	sumElement.textContent = "Sum: " + sum
	if (sum <= 20) {
		message = "Do you want to draw a new card?"
	} else if (sum === 21) {
		message = "You've got Blackjack!"
		hasBlackJack = true
	} else {
		message = "You're out of the game!"
		isAlive = false
	}
	messageElement.textContent = message
}

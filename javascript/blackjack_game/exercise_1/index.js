let firstCard = 10 
let secondCard = 4

let cards = [firstCard, secondCard]

let sum = firstCard + secondCard

let hasBlackJack = false
let isAlive = true
let message = ""

let messageElement = document.getElementById("message-element")
let sumElement = document.getElementById("sum-element")
let cardsElement = document.getElementById("cards-element")

function startGame() {
	renderGame()
}

function renderGame() {
	cardsElement.textContent = "Cards: " + cards[0] + " " + cards[1]
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

function newCard() {
	let card = 6
	sum += card
	renderGame()
}

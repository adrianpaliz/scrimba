let cards = []
let sum = 0

let hasBlackJack = false
let isAlive = false
let message = ""

let messageElement = document.getElementById("message-element")
let sumElement = document.getElementById("sum-element")
let cardsElement = document.getElementById("cards-element")

function getRandomCard() {
	let randomNumber = Math.floor( Math.random() * 13 ) + 1
	if (randomNumber > 10){
		return 10
	} else if (randomNumber === 1){
		return 11
	} else {
		return randomNumber
	}
}

function startGame() {
	isAlive = true
	let firstCard = getRandomCard()
	let secondCard = getRandomCard()
	cards = [firstCard, secondCard]
	sum = firstCard + secondCard
	renderGame()
}

function renderGame() {
	cardsElement.textContent = "Cards: "

	for (let index = 0; index < cards.length; index++) {
		cardsElement.textContent += cards[index] + " "
}

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
	let card = getRandomCard()
	sum += card
	cards.push(card)
	renderGame()
}

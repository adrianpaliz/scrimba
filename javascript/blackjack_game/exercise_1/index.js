let firstCard = getRandomCard() 
let secondCard = getRandomCard()

let cards = [firstCard, secondCard]

let sum = firstCard + secondCard

let hasBlackJack = false
let isAlive = true
let message = ""

let messageElement = document.getElementById("message-element")
let sumElement = document.getElementById("sum-element")
let cardsElement = document.getElementById("cards-element")

function getRandomCard() {
	let randomCard = Math.floor( Math.random() * 13 ) + 1
	if (randomCard === 1){
		return 11
	}	
	else if (randomCard === 11 || randomCard === 12 || randomCard === 13){
		return 10
	}
	else {
		return randomCard
	}
}


function startGame() {
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

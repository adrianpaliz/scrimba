let hands = ["rock", "paper", "scissor"]

function getRandomItem() {
	let randomIndex = Math.floor( Math.random() * 3 )
	return hands[randomIndex]
}

console.log(getRandomItem())

let hands = ["rock", "paper", "scissor"]

let randomNumber = Math.floor( Math.random() * 3 )

function randomItem() {
	if (randomNumber === 0) {
		return hands[0]
	} else if (randomNumber === 1) {
		return hands[1]
	} else {
		return hands[2]
	}
}

console.log(randomItem())

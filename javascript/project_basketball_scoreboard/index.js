let homeScore = document.getElementById("home-score")
let guestScore = document.getElementById("guest-score")

let homeCount = 0
let guestCount = 0

function incrementByOneToTheHome() {
	homeCount += 1
	homeScore.textContent = homeCount	
}

function incrementByTwoToTheHome() {
	homeCount += 2
	homeScore.textContent = homeCount
}

function incrementByThreeToTheHome() {
	homeCount += 3
	homeScore.textContent = homeCount
}


function incrementByOneToTheGuest() {
	guestCount += 1
	guestScore.textContent = guestCount
}

function incrementByTwoToTheGuest(){
	guestCount += 2
	guestScore.textContent = guestCount
}

function incrementByThreeToTheGuest(){
	guestCount += 3
	guestScore.textContent = guestCount
}

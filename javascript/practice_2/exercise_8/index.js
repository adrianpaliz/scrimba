let fruit = ["🍎", "🍊", "🍎", "🍎", "🍊"]
let appleShelf = document.getElementById("apple-shelf")
let orangeShelf = document.getElementById("orange-shelf")

function organizeFruits() {
	for (let index = 0; index < fruit.length; index++) {
		if (fruit[index] === "🍎") {
			appleShelf.textContent += "🍎" 
		} else if (fruit[index] === "🍊"){
			orangeShelf.textContent += "🍊" 
		}	
	}
}

organizeFruits()

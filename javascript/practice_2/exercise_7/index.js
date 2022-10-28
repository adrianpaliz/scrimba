let fighters = ["🐉", "🐥", "🐊","💩", "🦍", "🐢", "🐩", "🦭", "🦀", "🐝", "🤖", "🐘", "🐸", "🕷","🐆", "🦕", "🦁"]

let stageElement = document.getElementById("stage")
let fightButton = document.getElementById("fightButton")

fightButton.addEventListener("click", function() {
    let randomIndexOne = Math.floor( Math.random() * fighters.length )
	let randomIndexTwo = Math.floor( Math.random() * fighters.length ) 
	stageElement.textContent = fighters[randomIndexOne] + " vs " + fighters[randomIndexTwo]
})

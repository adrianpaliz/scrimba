let data = [
	{
		player: "Maria",
		score: 52	
	},
	{
		player: "Enrique",
		score: 41
	}
]

const scoreButton = document.getElementById("maria-score-button")

scoreButton.addEventListener("click", function(){
	playerOneScore = data[0].score
	console.log(playerOneScore)
})

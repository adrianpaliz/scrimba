const containerElement = document.getElementById("container")

containerElement.innerHTML = "<button onclick='buy()'>Buy!</button>"

function buy() {
	containerElement.innerHTML += "<p>Thank you for buying!</p>"
}

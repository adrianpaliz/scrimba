let sentence = ["Hello", "my", "name", "is", "Adrián"]
let greetingElement = document.getElementById("greeting-element")

for ( let index = 0; index < sentence.length; index++ ) {
	greetingElement.textContent += sentence[index] + " "
}

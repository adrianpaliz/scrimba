let number1 = 8
let number2 = 2
document.getElementById("number1-element").textContent = number1
document.getElementById("number2-element").textContent = number2

// Create four functions: add(), subtract(), divide(), multiply()
// Call the correct function when the user clicks on one of the buttons
// Perform the given calculation using num1 and num2
// Render the result of the calculation in the paragraph with id="sum-el"

// E.g. if the user clicks on the "Plus" button, you should render
// "Sum: 10" (since 8 + 2 = 10) inside the paragraph with id="sum-el"
let sumElement = document.getElementById("sum-element")
console.log(sumElement)

function add() {
	console.log("Button Add clicked")
	console.log(sumElement.textContent)
	sumTotal = number1 + number2
	sumElement.textContent ="Sum: " + sumTotal
	console.log(sumElement.textContent)
}

function subtract() {
	subtractTotal = number1 - number2
	sumElement.textContent = "Sum: " + subtractTotal
}

function divide() {
	divideTotal = number1 / number2
	sumElement.textContent = "Sum: " + divideTotal
}

function multiply() {
	multiplyTotal = number1 * number2
	sumElement.textContent = "Sum: " + multiplyTotal
}

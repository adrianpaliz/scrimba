// The generateSentence(desc, arr) takes two parameterer: a description and an array.
// It should return a string based upon the description and array.

// Example 1: if you pass in "largest countries",and ["China", "India", "USA"],
// it should return the string: "The 3 largest countries are China, India, USA"

// Use both a for loop and a template string to solve the challenge

function generateSentence(description, array) {
	let baseString = `The ${array.length} ${description} are `
	for (let index = 0; index < array.length; index++){
		baseString += array[index] + ", "
	}
	return baseString
}

const sentence = generateSentence("Ecuador main export products", ["crude oil", "shrimp", "bananas"])
console.log(sentence)

// Create a function that renders the three team images
// Use a for loop, template strings (``), plus equals (+=)
// .innerHTML to solve the challenge.

const imagesContainer = document.getElementById("images-container")

const images = [
    "images/writer1.jpg",
    "images/writer2.jpg",
    "images/writer3.jpg"
]

function renderImages(){
	let imagesDOM = ""
	for (let index = 0; index < images.length; index++){
		imagesDOM +=`<img alt="Ecuadorian writer" class="writer-image" src="${images[index]}">`
	}
	imagesContainer.innerHTML = imagesDOM
}

renderImages()

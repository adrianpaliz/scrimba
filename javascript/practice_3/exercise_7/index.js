// Challenge:
// The toFixed() method doesn't work anymore. Can you make it work?
// Google the error message if you're unsure about how to do it

const totalPrice = "420.69235632455"
const button = document.getElementById("purchase-button")
button.textContent = `Buy $${ Number(totalPrice).toFixed(2) }` 

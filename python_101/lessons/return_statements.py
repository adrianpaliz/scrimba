print("Return statements")

def value_added_tax(amount):
    tax = amount * 0.25
    total_amount = amount * 1.25
    #return tax
    #return amount, tax, total_amount
    #return [amount, tax, total_amount] <-- Return a list
    #return {amount, tax, total_amount} <-- Return a set
    return f"{amount}, {tax}, {total_amount}" #<-- Return a string
price = value_added_tax(100)

#print(price, type(price)) 
#print(price[1], type(price)) 
print(price, type(price))

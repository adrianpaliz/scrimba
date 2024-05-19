print("Return statements")

def value_added_tax(amount):
    tax = amount * 0.25
    total_amount = amount * 1.25
    #return tax <-- Return a float
    #return amount, tax, total_amount <-- Return a tuple
    #return [amount, tax, total_amount] <-- Return a list
    #return {amount, tax, total_amount} <-- Return a set
    return f"{amount}, {tax}, {total_amount}" #<-- Return a string
price = value_added_tax(100)

#print(price, type(price)) <-- Print a float and his type
#print(price[1], type(price)) <-- Print a items of the list
print(price, type(price))

freelancers = {
  'name' : 'freelancing Shop',
  'brian' : 70,
  'black knight' : 20,
  'biccus diccus' : 100,
  'grim reaper' : 500,
  'minstrel' : -15
}

antiques = {
  'name' : 'Antique Shop',
  'french castle' : 400,
  'wooden grail' : 3,
  'scythe' : 150,
  'catapult' : 75,
  'german joke' : 5
}

pet_shop = {
  'name' : 'Pet Shop',
  'blue parrot' : 10,
  'white rabbit' : 5,
  'newt' : 2
}

cart = {
}
stores = (freelancers, antiques, pet_shop)
for dictionary in stores:
    list_items = list(dictionary.keys())[1:]
    
    buy_item_key = input(f'Welcome to {dictionary['name']}! What do you want to buy: {list_items} ')
    buy_item_key = buy_item_key.lower()
    buy_item_value = dictionary.pop(buy_item_key)
    
    cart.update({buy_item_key : buy_item_value})
print(cart)


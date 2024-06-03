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

purse = 1000
spend = 0
items_list = ''
for dictionary in stores:
    list_items = list(dictionary.keys())[1:]
    
    buy_item_key = input(f'Welcome to {dictionary['name']}! What do you want to buy: {list_items} ')
    
    if buy_item_key in list_items:
    
        buy_item_key = buy_item_key.lower()
        
        items_list += f'{buy_item_key} : {dictionary[buy_item_key]} gold pieces, '
        
        buy_item_value = dictionary.pop(buy_item_key)
    
        cart.update({buy_item_key : buy_item_value})
        
        spend += int(buy_item_value)

        gold_left_over = purse - int(buy_item_value)
        
        buy_items_list = ', '.join(list(cart.keys()))
        print(f'{buy_item_key} was added to the cart')

    elif buy_item_key == 'exit':
        print('Goodbye')
        continue
    else:
        print(f'The item {buy_item_key} does not exist')
        continue

print(f'You purchased: {items_list}. Today you spend {spend} and have {gold_left_over} of gold pieces left over. Have a nice day of mayhen!')


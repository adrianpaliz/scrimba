def greeting(name, age = 34, color = "red"):
 #Greets user with 'name' from 'input box' and 'age', if unavailable, default age is used
    print(f'Hello {name.capitalize()}, you will be {age+1} next birthday!')
    print(f"We hear you like the color {color.lower()}!")

greeting(age = 27, name = "Adrián", color = "Blue")



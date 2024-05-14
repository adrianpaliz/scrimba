message = "Welcome to Python 101: Split and Join"
#print(list(message))
#split() method split appart the message string in a list, separated by white spaces
print(message.split())
#print(message.split(" "))
print("".join(message.split()))
print(message.replace(" ", ""))


comma_separated_values = "María,Adrián,Guillermo,Alejandra"
print(comma_separated_values.split(","))


friends_list = ["María", "Adrián", "Guillermo", "Alejandra"]
print("-".join(friends_list))
print("-".join(friends_list + friends_list))
print("".join(friends_list))


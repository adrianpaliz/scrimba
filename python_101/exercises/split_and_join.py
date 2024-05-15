comma_separated_values = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'

#Solution 1
#string_1 = comma_separated_values.replace(":",",")
#string_2 = string_1.replace(";", ",")
#friends_list = (string_2.split(","))
#print(friends_list)

#solution 2
friends_list = (comma_separated_values.replace(":",",").replace(";",",").split(","))

print(friends_list)

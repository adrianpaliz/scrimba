#Sets - Exercise

#1. Check if ‘Eric’ and ‘John’ exist in friends
#2. combine or add the two sets 
#3. Find names that are in both sets
#4. find names that are only in friends
#5. Show only the names who only appear in one of the lists
#6. Create a new cars-list without duplicates

#1
friends = {"John","Michael","Terry","Eric","Graham"}
print("Eric" in friends)
print("John" in friends)
#print("Eric" in friends and "John" in friends)

#2
my_friends = {"Reg","Loretta","Colin","John","Graham"}
union_set = friends.union(my_friends)
print(union_set)
#print(friends | my_friends)

#3
intersection_set = friends.intersection(my_friends)
print(intersection_set)
#print(friends & my_friends)

#4
difference_set = friends.difference(my_friends)
print(difference_set)
#print(friends - my_friends )

#5
symmetric_difference_set = friends.symmetric_difference(my_friends)
print(symmetric_difference_set)
#print(friends ^ my_friends)

#6
cars =["900","420","V70","911","996","V90","911","911","S","328","900"]
cars_no_duplicates = list(set(cars))
print(cars_no_duplicates)

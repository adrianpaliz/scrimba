python = {
  'John' : 35,
  'Eric' : 36,
  'Michael' : 35,
  'Terry' : 38,
  'Graham' : 37,
  'TerryG' : 34
}

holy_grail = {
  'Arthur' : 40,
  'Galahad' : 35,
  'Lancelot' : 39,
  'Knight of NI' : 40,
  'Zoot' : 17
}
life_of_brian = {
  'Brian' : 33,
  'Reg' : 35,
  'Stan/Loretta' : 32,
  'Biccus Diccus': 45
}

#menbership test
print('arthur' in holy_grail) #Return False because is case sensitive
print('Arthur' in holy_grail)

if 'Arthur' not in python:
    print('He\'s not here!')

if 'Arthur' in python: 
    print('He\'s not here!') #Deson't print anything because if evalues to False

#Concatinating dictionaries 
people = {
}
people_1 = {
}
people_2 = {
}

#Method 1 update
people.update(python)
print(people)
people.update(holy_grail)
print(people)
people.update(life_of_brian)
print(sorted(people))

#Method 2 comprehension
for groups in (python, holy_grail, life_of_brian) : people_1.update(groups)
print(sorted(people_1.items()))

#Method 3 unpacking 
people_2 = {**python, **holy_grail, **life_of_brian}
print(sorted(people_2)) 

print('The sum of the ages: ', sum(people.values()))


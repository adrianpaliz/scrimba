print("Dictonaries")

movie = {
  'title' : 'Movie momments in real life',
  'year' : '2024',
  'cast' : ['Adrián', 'Isabel', 'Jessica', 'Jordan']
  }

print(movie)
print(movie['title'])

#print(movie['budget']) # We get a error
print(movie.get('budget')) # We get a none
print(movie.get('budget', 'not found')) #Print a message

movie['title'] = 'Real moments'
print(movie.get('title'))

movie['budget'] = 250000
print(movie)

movie.update({'title' : 'Movie momments in real life', 'year' : 2024, 'cast' :  ['Adrián', 'Isabel', 'Jessica', 'Jordan']})
print(movie)

del movie['year']
print(movie)

budget = movie.pop('budget')
print(movie)
print(budget)

print(len(movie))
print(movie.keys())
print(movie.values())
print(movie.items())

for key in movie:
    print(key)

for key, value in movie.items():
    print(key, value)


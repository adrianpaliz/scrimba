movies = ["UIO, Sácame a pasear", "La mala noche", "Cronicas", "Sumergible", "Cenizas", "A tus espaldas"]
years = [2016, 2019, 2004, 2020, 2018, 2011]
directors = ["Micaela Rueda", "Gabriela Calvache", "Sebastian Cordero", "Alfredo León", "Juan Jacome", "Tito Jara"]
#Printinh as a list
#print(list(zip(movies, years)))
#Give me a dict('movie': year) for each movie, year in zip(movies, years)
'''
new_dictionary = dict()
for movie, year in zip(movies, years):
    new_dictionary[movie] = year
print(new_dictionary)
'''
#Using dictionary comprehension
'''
new_dictionary = {movie : year for movie, year in zip(movies, years)}
print(new_dictionary)
'''
#Adding a if statement
'''
new_dictionary = {movie : year for movie, year in zip(movies, years) if year < 2019 and movie.startswith('C')} 
print(new_dictionary)
'''
#Printing also the director name
'''
movie_info = [(director, movie, year) for director, movie, year in zip(directors, movies, years) if year > 2018]
print(movie_info)
'''
#Adding text to make a information string
movie_info = [[director + ' directed the film: ' + movie + ' from ' + str(year)] for director, movie, year in zip(directors, movies, years) if year > 2018]
print(movie_info)

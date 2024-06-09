
#Calses are blueprints
#Objects are the actual things you built
#Variables  => attributes
#Functions => methods

class Movie:
    def __init__(self, title, year, imdb_score, have_seen):
        self.title = title
        self.year = year
        self.imdb_score = imdb_score
        self.have_seen = have_seen

    def nice_print(self):
        print("Title:", self.title)
        print('Year of production:', self.year)
        print('IMDB Score:', self.imdb_score)
        print('I have seen it:', self.have_seen)

film_1 = Movie("Sensaciones", 1991, 7.2, True)
film_2 = Movie("Cuando me toque a mi", 2006, 6.5, True)

#print(film_1.title, film_1.imdb_score)

#film_2.nice_print()
#Movie.nice_print(film_2)

films = [film_1, film_2]
print(films[1].title, films[0].title)
films[0].nice_print()




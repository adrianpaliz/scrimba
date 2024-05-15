friends_list = ['John','Michael','Terry','Eric','Graham']
friends_tuple = ('John','Michael','Terry','Eric','Graham')
friends_set = {'John','Michael','Terry','Eric','Graham','Eric'}

print(friends_list)
print(friends_tuple)
print(friends_set)

my_friends_set = {'Reg','Loretta','Colin','Eric','Graham'}

print(friends_set.intersection(my_friends_set))
print(friends_set.difference(my_friends_set))
print(friends_set.union(my_friends_set))

#Empty list
empty_list = []
empty_list = list()
#Empty tuple
empty_tuple = ()
empty_tuple = tuple()
#Empty set
empty_set = {} # This is wrong, this is a dictionary
empty_set = set()

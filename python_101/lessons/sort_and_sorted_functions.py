print('sort() and sorted()')
print('Immutability and return values')

my_list = [1, 5, 3, 7, 2]
my_dict = {
  'car' : 4,
  'dog' : 2,
  'add' : 3,
  'bee' : 1
        }
my_tuple = ('d','c','e','a','b')
my_string = 'python'

print(my_list, 'original list')

print(my_list.sort()) #Print None
print(my_list, 'previous list using sort()')

print(my_list.reverse()) #Print None
print(my_list, 'reverse, non\'t reverse order')

print(sorted(my_list)) #Print a new list
print(my_list, 'using sorted')
my_sorted_list = sorted(my_list)
print(my_sorted_list, 'printing the new object that sorted() create')
print(reversed(my_list)) #Print a reversed object
print(list(reversed(my_list)), 'Print the reversed object that was converted in a list')
print(my_list[::-1], 'Do the same that reversed')


#Printing the sorted version of a tuple
print(my_tuple, 'original tuple')
print(sorted(my_tuple)) #sorted applied to a tuple print a list
print(my_tuple, 'Equal to the original one, because a list was created previously')

#Printing a string
print(my_string, 'original')
print(sorted(my_string)) #print a new object, a list
print(my_string, 'Equal to the original one')

#Printing a dictionary
print(my_dict, 'original')
print(sorted(my_dict), 'Just the key values were sorted')
print(my_dict, 'Equal to the original')

print(sorted(my_dict.items()), 'We get a tuples inside a list sorted by key')
print(sorted(my_dict.values()), 'Just the values sorted')
print(sorted(my_dict.values(), reverse = True), 'The values in reverse order')


my_list_values = [1,5,-3,7,-2]
list_of_list=[['car',4,65],['dog',2,30],['add',3,10],['bee',1,24]]

print(sorted(my_list_values), 'Print the spected order')
print(sorted(my_list_values, key = abs), 'Print the absolute order regardless of the sign')

print(sorted(list_of_list))
print(sorted(list_of_list, key = lambda item :item[1]))


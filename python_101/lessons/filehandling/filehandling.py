#my_file = open('python_101/lessons/filehandling/greeting.txt', 'r')
# print(my_file.read()) #Read the whole file
# print(my_file.read(10)) #Read the ten first characters
#print(my_file.readline()) #Read the first line, if this line is next to a equal line that will print the second line

#line_by_line = my_file.readlines()
#print('Readlines: ', line_by_line)

#line_by_line_1 = my_file.read().splitlines()
#print('Splitlines: ', line_by_line_1)
#my_file.close() 

'''
with open('python_101/lessons/filehandling/friends.csv', 'r') as my_file:
    #print(my_file.read())
    
    friends = my_file.read().splitlines()
    #print(friends)

    for friend in friends:
        friend = friend.split(',')
        name = friend[0]
        year = int(friend[1].strip()) 
        print(f'In 2030 {name} will be {2030 - year} years old')
'''

with open('python_101/lessons/filehandling/movies.txt', 'r') as my_file:
    #for line in my_file:
    #    print(line)
    for line in my_file.readlines():
        print(line)


library = ["Books", "Chairs", "Newspapers", "Tables", "Computers"]
print(library)
library.sort()
print(library)
library.sort(reverse = True)
print(library)
library.reverse()
print(library)
library.append("Magazines")
print(library)
library.insert(1, "Stairs")
print(library)
library[3] = "Archive"
print(library)
library.remove("Newspapers")
print(library)
library.pop()
print(library)
library.pop(2)
print(library)
library.pop(-1)
print(library)
#library.clear()
#print(library)
#del library
#print(library)
del library[2]
print(library)

#Coping lists
new_library = library[:]
print(new_library)
another_library = library.copy()
print(another_library)
another_2_library = list(library)
print(another_2_library)

models = [434, 920, 674, 112, 300, 902]
print(models)
models.sort()
print(models)
models.sort(reverse = True)
print(models)
models.reverse()
print(models)
print(min(models))
print(max(models))
print(sum(models))
library.extend(models)
print(library)

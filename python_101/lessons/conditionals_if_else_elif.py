#First explanation about True conditional
'''
is_raining = True
print("Good morning")
if is_raining:
    print("Bring a umbrella")
'''

#Second explanation about False conditional and else
'''
is_raining = False
print("Good morning")
if is_raining:
    print("Bring a umbrella")
else:
    print("Umbrella is optional")
'''

#Third explanation about "or" boolean operator
'''
is_raining = True
is_cold = False 
print("Good morning")
if is_raining or is_cold:
    print("Bring a umbrella or jacket or both")
else:
    print("Umbrella is optional")
'''

#Fourth explanation about "and" boolean operator
'''
is_raining = False 
is_cold = False
print("Good morning")
if is_raining and is_cold:
    print("Bring umbrella and jacket")
else:
    print("Umbrella is optional")
'''

#Fiveth explanation about "not" boolean operator
'''
is_raining = False
is_cold = True
print("Good morning")
if is_raining and is_cold:
    print("Bring umbrella and jacket")
elif is_raining and not (is_cold):
    print("Bring umbrella")
elif not(is_raining) and is_cold:
    print("Bring jacket")
else:
    print("Shirt is fine!")
'''

#Example 
amount = 51
if amount <= 50:
    print("Purchasa approved")
else:
    print("Please enter your pin!")


message = "welcome to Python 101: Strings"

string = (message[18] + " " + message[:8] + message[-5:-1] + message[7:11] + message[13] + message[12] + message[2] + message[1] + message[-5])

titled_string = string.title()
print(titled_string)

string_3 = titled_string[::-1]
print(string_3)


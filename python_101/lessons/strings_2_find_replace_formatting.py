message = """Every day,
I learn something new 
about tmux <3
"""
print(message)

message_2 = "Welcome to Python 101: Strings"
print(message_2.find("h"))
print(message_2.replace("Python", "JavaScript"))

message_3 = message_2.replace("Python", "JavaScript")
print(message_3)

print("Python" in message_2)
print("Python" not in message_2)

name = "ADRIÁN"
color = "YELLOW"
message_4 = "[" + name + "] loves the color " + color.lower() + "!"
print(message_4)
message_5 = f"[{name.capitalize()}] loves the color {color.lower()}!"
print(message_5)


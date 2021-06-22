# Program 3 - Formatted String
name = "Hasan"
language = 'Python'
message = "My name is '"+name+"'. I am learning '"+ language + "'"
msg = f'My name is "{name}". I am learning "{language}"' #Formatted Text starts with f''
print(message)
print(msg)

# Program 4 - Count Length of Array/String

print(len(msg))
print(msg.upper())
print(msg.lower())
print(msg.capitalize())
print(msg.title())
print(msg.find('i')) # Find and return index
print(msg.replace("learning", "started learning")) # Find and replace string
print('name' in msg) # Find and return boolean. "in" returns boolean true or false

num = 225
num2 = 22
num3 = 22
if num==num2:
    print("Comparison is true")
elif num3 == num2:
    print("Equal Number")
else:
    print("Not matched")

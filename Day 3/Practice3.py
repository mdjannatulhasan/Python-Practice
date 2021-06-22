# Program 5 - While Loop
# command = ""
# commandCountStart = 0
# commandCountStop = 1
# print("Enter your command or type 'Help'")
# while True:
#     command = input("> ").lower()
#     if command == "start" and commandCountStart == 0:
#         print("Car Started.... ")
#         commandCountStart+=1
#         commandCountStop = 0
#     elif command == "start" and commandCountStart > 0:
#         print("Car already started.....")
#     elif command == "stop" and commandCountStop == 0:
#         print("Car Stopped!!!")
#         commandCountStart = 0
#         commandCountStop+=1
#     elif command == "stop" and commandCountStop > 0:
#         print("Car stopped already. What are you doing!??? ")
#     elif command == "help":
#         print("""
# Start - to start the car
# Stop - to stop the car
# Quit - to stop the programme
#         """)
#     elif command == "quit":
#         print("Bye Bye")
#         break
#     else:
#         print("I don't understand")

# Programmme 6 - For loops
alphabetArray = [1, 2, 2, 7, 2]
alphabetArraySpaces = [[4, 0], [3, 1], [2, 3], [1, 0], [0, 7]]
alphabet = "A"
for i in range(len(alphabetArray)):
    print(" " * alphabetArraySpaces[i][0], end="")
    if alphabetArray[i] > 2:
        print(alphabet*(alphabetArray[i]-1), end="")
    elif alphabetArray[i] != 1:
        print(alphabet, end="")
    if alphabetArraySpaces[i][1] != 0:
        print(" "*alphabetArraySpaces[i][1], end="")
    print(alphabet + " " * alphabetArraySpaces[i][0])

print("    A")
print("   A A")
print("  A   A")
print(" AAAAAAA")
print("A       A")
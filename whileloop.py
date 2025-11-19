#Tis files covers: While-loops and userinput, f-strings, comparison operators,logical operator

#Example 1
name = input("Enter your name: ")

while name == "":  #Tom sträng betyder att du inte angav något tecken
    print("You did not enter your name")
    name = input("Please enter your name: ")    #Uppmaningen försvinner tills namn har uppgetts
    #Om inte feedbacken ovan funnits skulle while-loopen bli oändlig
print(f"Hello {name}")
print("\n")

#Example 2
age = int(input("Enter your age: "))

while age < 0:  #Så länge detta villkor är sant pågår loopen
    print("Age can´t be negative")
    age = int(input("Enter your age: "))    #casting = åldern anges som ett heltal
print(f"You are {age} years old")   #Villkoret är falskt och man kommer ur loopen
print("\n")

#Example 3
food = input("Enter a food you like (q to quit): ")

while not food == "q":  #Så länge som användaren INTE anger "q" körs loopen
    print(f"You like {food}")   
    food = input("Enter another food you like (q to quit): ")   #Följdfråga inne i loopen. Nu körs loopen från början, dvs. rad 26 
print("The programme now shuts down") #Nu har användaren angett "q"
print("\n")

#Example 4
num = int(input("Enter a number between 1-10: "))

while num < 1 or num > 10:
    print("Your number is not valid")
    num = int(input("Enter a number between 1-10: "))
print(f"Your number is {num}")
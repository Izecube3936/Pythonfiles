
#Content: input, casting, f-strings with modifier, expressions


name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in cm: "))
#age = age + 1   Koden kommer inte att funka eftersom man inte kan konkatanera strängar
# age = int(age)  casting, som innebär att vi gör om heltal nu kan lagras i varabeln age istället. 
#Dock skriver man mindre kod om man på en rad (rad 2) anger att age = int 
age = age + 1   #Nu fungerar koden som lägger till +1
print(f"Hello {name}")
print(f"You are {age} years old")
print(f"Your height is {height:.2f} cm")    #Placeholder with modifier, dvs. två decimaler
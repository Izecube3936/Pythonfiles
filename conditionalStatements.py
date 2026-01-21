#Content: Conditional expressions (if and else statements) and logical operators

#Exempel 1

num1 = 5
print(f"Number {num1} is positive\n " if num1 > 0 else f"Number {num1} is neagative\n ")  #Allt skrivs på en rad här jämfört med nästa exempel

#Exempel 2

num2 = 8
result = f"Number {num2} is even\n " if num2 % 2 == 0 else f"Number {num2} is odd\n "
print(result)

#Exempel 3

num3 = 10
num4 = 8
max_num = num3 if num3 > num4 else num4  #I detta uttryck är variablerna operander
print(f"The largest number is {max_num}")  #10 är det största talet
print("\n") #På detta vis kan man också ange ny rad

#Exempel 4

age = 25
status = "adult" if age >= 18 else "child"
print(f"You are an {status}") #Om man anger "age" som variabel visas åldern, inte "Adult/Child"
print("\n")


#Exempel 5

temperature = 34
weather = print("It´s hot") if temperature >25 else print("It´s warm") if temperature == 25 else print("It´s quite warm")if temperature >18 and temperature <25 else  print("Not varm enough")  
#Fyra olika villkor, där det näst sista fångar in om temperaturen >18 grader och <25 grader. Istället för att skriva/printa 
#ut resultatet på sista raden, har jag här valt tre olika print-anrop på en rad
print("\n")

user_role = "admin" #Variabeln är här en sträng och inte en siffra
access_level = "Full access" if user_role == "admin" else "Limited access" if user_role == "guest" else "Access denied"
#Åter tre olika villkor. Här måste man ha angett exakt "admin" eller "guest" för att få någon tillgång till systemet.
print(f"Your access level is: {access_level}")


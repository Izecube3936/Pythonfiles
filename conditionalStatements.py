#Conditional expressions, logical operators

num1 = -5
print("Positive\n " if num1 > 0 else "Neagative\n ")  #Allt skrivs på en rad här jämfört med nästa exempel

num2 = 8
result = "Even\n " if num2 % 2 == 0 else "Odd\n "
print(result)

num3 = 10
num4 = 8
max_num = num3 if num3 > num4 else num4#I detta uttryck är variablerna operander
print(max_num)  #10 är det största talet
print("\n") #På detta vis kan man också ange ny rad

age = 25
status = "Adult" if age >= 18 else "Child"
print(status) #Om man anger "age" som variabel visas åldern, inte "Adult/Child"
print("\n")

temperature = 34
weather = print("Hot") if temperature >25 else print("Warm") if temperature == 25 else print("Quite warm")if temperature >18 and temperature <25 else  print("Not varm enough")  
#Fyra olika villkor, där det näst sista fångar in om temperaturen >18 grader och <25 grader. Istället för att skriva/printa ut resultatet på sista raden, 
# Shar jag här valt tre olika print-anrop på en rad
print("\n")

user_role = "admin" #Variabeln är här en sträng och inte en siffra
access_level = "Full access" if user_role == "admin" else "Limited access" if user_role == "guest" else "Access denied"
#Åter tre olika villkor. Här måste man ha angett exakt "admin" eller "guest" för att få någon tillgång till systemet.
print(access_level)


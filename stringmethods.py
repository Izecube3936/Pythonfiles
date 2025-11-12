#Stringmethods: upper(), len(), find(), rfind(), isdigit(), isalpha(), count(), replace(), 

name = input("Enter your full name: ")
password = input("Enter your password: ")
phone_nr = input("Enter your phone number: ")
social_security_nr = input("Enter your social security number: ")
print("\n")

#Variabeln name
name = name.upper() #Namnet skrivs med versaler
result = len(name)  #Anger hur många bokstäver mitt namn består av
space = name.find(" ") #Om du har angett ett namn med mellanslag (Jan Erik)kan find-metoden användas för att avgöra var
# det finns. Index 0 = första bokstaven.
result2 = name.rfind("r")   #Heter man Fredrik visas index 4 eftersom det är den senaste förekomsten av "r"
result3 = name.isalpha() ##Endast om ditt namn består av bokstäver anges "True", annars "False" - om du anger mellanslag 
# får du dock utskriften "False"

#Variabeln password
result4 = password.isdigit() #Bara om du angett att ditt lösen består av siffror anges "True", annars "False"

#Variabeln phone_nr
result5 = phone_nr.count("0")   #String måste anges här för att räkna förekomsten av siffran 0
result6 = phone_nr.replace("-", " ")    #Metoden ersätter "-" med tomrum

#Variabeln social_security_nr
result7 = social_security_nr.replace("-", "")   #Metoden gör att alla "-" raderas och att personnr. skrivs löpande

print(f"Your name is {name}")     #Namnet med versaler
print(f"Your name has {result} characters")   #Om du heter Jan Erik har mellanslagen inkluderats
print(f"The first space occurs at index {space}") #Om du angett Fredrik, som inte har ett mellanslag, anges här -1.
# Det betyder att inget mellanslag identifieras.
print(f"The last occurens at the letter r is at index {result2}")
print(result3)
print("\n")


print(result4)
print("\n")

print(f"Your phone number has {result5} occurrens of the number 0")
print(f"Your phone number now hasn´t got any dashes: {result6}")
print("\n")

print(f"Your social security number now hasn´t got any dashes or spaces: {result7}")

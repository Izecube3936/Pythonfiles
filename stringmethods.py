#Content: stringmethods such as upper(), len(), find(), rfind(), isdigit(), isalpha(), count(), replace() 

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

r_letter = name.rfind("r")   #Heter man Fredrik visas index 4 eftersom det är den senaste förekomsten av "r"

boolean1 = name.isalpha() ##Endast om ditt namn består av bokstäver anges "True", annars "False" - om du anger mellanslag 
# får du dock utskriften "False"

#Variabeln password
boolean2 = password.isdigit() #Bara om du angett att ditt lösen består av siffror anges "True", annars "False"

#Variabeln phone_nr
nr0 = phone_nr.count("0")   #String måste anges här för att räkna förekomsten av siffran 0
result6 = phone_nr.replace("-", " ")    #Metoden ersätter "-" med tomrum

#Variabeln social_security_nr
result7 = social_security_nr.replace("-", "")   #Metoden gör att alla "-" raderas och att personnr. skrivs löpande

print(f"Your name is {name}")     #Namnet med versaler
print("\n")

print(f"Your name has {result} characters")   #Om du heter Jan Erik har mellanslagen inkluderats
print("\n")

print(f"The first space occurs at index {space}") #Om du angett Fredrik, som inte har ett mellanslag, anges här -1.
# Det betyder att inget mellanslag identifieras.
print("\n")

print(f"The last occurens at the letter r is at index {r_letter}")
print("\n")

print("If your output is \"True\" it means that you typed letters only. However, if you entered a space or another character you´ll get the output \"False\"." 
f"Your output is: {boolean1}.") 
print("\n")


print("If your output is \"True\" it means that your password consist of numbers only. However, if you entered a space or another character you´ll get the output \"False\"." 
f"Your output is: {boolean2}.")
print("\n")

print(f"Your phone number has {nr0} occurrens of the number 0")
print("\n")
d
print(f"Your phone number now hasn´t got any dashes: {result6}")
print("\n")

print(f"Your social security number now hasn´t got any dashes or spaces: {result7}")

#Filen omfattar: primitiva datatyper, typecasting, type-metoden, additional assignmentoperator, 


#Primitiva datatyper
name = "Fredrik"
age = 47
grade = 4.2
is_student = True

print(type(name))   #Type metoden ger svar på variablernas datatyp
print(type(age))
print(type(grade))
print(type(is_student))

grade = int(grade)  #Typecasting: 4.2. omvandlas till heltalet 4
age = str(age)  #Variablens värde är fortfarande 47 men datatypen är nu en sträng
name = bool(name)   #Utskriften blir True om datatypen är strängar, flytttal eller heltal
# Däremot skulle outputen bli False om variabeln name = " " (tom sträng). Skulle t.ex. kunna användas för att kontrollera
# att någon anger sitt namn!

print(grade)    
print(age)  
print(name)

age += "1"  #Fungerar eftersom "1" och age är strängar, men resultat blir märkligt
print(age)  #När jag skriver ut värdet nu blir resultatet inte 47 utan 471

new_age = 47 + 4.1  #Det fungerar att summera heltal och flyttal
#Däremot skulle inte följande s.k. expression fungera: new_age = age + grade
print(new_age)
print(type(new_age))    #Datatypen är nu float


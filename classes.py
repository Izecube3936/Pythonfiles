#Content: creating of classes with values and parameters, the init-method, creating of objects,
#methods belonging to classes, the use of classes, positionell arguments

#Exempel 1

class MyClass:  #Klassen skapas
  x = "Min första klass"    #x (som inte kan vara en siffra) är en property som hör till klassen "MyClass"

MyC = MyClass()  #Med hjälp av klassen "MyClass" skapas ett objekt
print(MyC.x) #Värdet x skrivs ut, dvs. texten "Min första klass"

#Exempel 2

class Person:   #Utifrån klassen "Person" skapas en s.k. ritning för att skapa olika objekt
  def __init__(self, name, age, minister, country = "Sweden"):  #Med hjälp av init-metoden skapas fyra properties/variabler:
 #name, age, minister och country. Init-metoden anropas automatiskt varje gång klassen används för att skapa ett nytt objekt.
 #Default-värdet måste komma sist - annars funkar det inte. Parametern self måste alltid stå först. 
    self.name = name    
    self.age = age  
    self.minister = minister
    self.country = country  #parametern "country" ovan har "Sweden" som defaultvärde
      
  def info_Bildt(self):
      print(f"{p1.name}, {p1.age} years old, has been {p1.minister} of {p1.country}")
      #Även om funktionen föregår skapandet av objektet (rad 23), kan argumenten användas
      
  def info_Carlsson(self):
      print(f"{p2.name}, {p2.age} years old, has also been {p1.minister} of {p1.country}")

p1 = Person("Carl Bildt", 76, "Prime Minister") #Klassen "Person" används här för att skapa objektet p1
# ,som här är en förkortning för person 1. Objektet har tre värden/argument. Eftersom "Sweden" är
# defaultvärde för parmetern "country" behöver detta land inte anges här.
  
p2 = Person("Ingvar Carlsson", 91, "Prime Minister")   #Init-metoden anropas automatiskt. Även om jag i funktionen 
# info_Carlsson(self) inte använder mig av p2.minister - utan av p1.minister - måste jag ha "Prime Minister" här som  
# en parameter eftersom det är ett positionellt argument.

p1.info_Bildt()#Funktionsanrop för person 1
p2.info_Carlsson()#Funktionsanrop för person 2
#del p2 = p2-objektet med dess argument raderas, och jag kan inte använda det mer

#Exempel 3

class Tennisplayer:
  lessons = 4   #Ett klassattribut, vilket kan delas av de två objekt som skapas nedan
  def __init__(self, fname, lname): #fname och lname kallas för instansattribut eftersom de används när klassen instansieras (rad 54)
    self.firstname = fname  #fname attributet döps nu om till firstname, vilket sedan används i funktionen nedan
    self.lastname = lname
    
  def greet(self):
    print(f"Welcome {self.firstname} {self.lastname} to this tenniscourse! It consists of {self.lessons} lessons.") 

player1 = Tennisplayer("Tobias", "Andersson")   #Ett objekt skapas med två värden = klassen har nu instansieras
player1.greet()
player2 = Tennisplayer("Fanny", "Alexandersson")
player2.greet()






#Content: while true-loops, f-strings, assignment operator, 
# comparison operator,  break, input, if- and else statements, time module

#Exempel 1:
def while_true_loop():
    counter = 0 #Det initiala värdet på räknaren
    
    while True:
        print(f"This loop will never count to 10. Counting: {counter}") 
        counter += 1    #Assignment operator, detsamma som counter = counter + 1
        if(counter == 10):  #Loopen körs tills villkoret inte längre är sant: när räknaren når 10
            break   #Vid 10 bryts loopen 
while_true_loop()   #Skriver ut siffrorna 0-9 - ej 10 eftersom räknarens initiala värde var 0
print("Nu är vi inte längre i loopen")
print("\n")

#Exempel 2:
def while_true_loop():  #Samma namn på en funktion kan användas fler gånger
    while True:
        name = input("Enter a name or enter quit, if you want to quit: ")
        if name.lower() == "quit":  #Även om du anger "quit" eller "Quit" kommer det att fungera pga. lower()-metoden
            print(f"Eftersom du har angett {name} avbryts loopen")
            break   #Loopen avbryts och programmet avlslutas
            
        else:
            print(f"Hello {name}!") #Här är du fortfarande i loopen
            
while_true_loop()
print("\n")

#Exempel 3
import time #Importerar time-modulen

def while_true_loop():  
    counter = 0 #Räknarens initiala värde
    start = input("Hit any key to start!")  #Detta uttryck måste stå utanför loopen eftersom det bara ska köras en gång
    
    while True:
        print(f"Counting {counter}")    #Skriv ut efter varje varv av loopen
        counter = counter + 1   #Värdet ökas efter varje loop med +1
        time.sleep(2)   #Till time-metoden knyts en metod som låter oss välja hur många s. som programmet ska pausas
        
        if counter == 8:    #När räknaren når 8 avbryts loopen...
            print("Now you´re out of the loop") #...men först skrivs detta meddelande ut
            break
            

while_true_loop()

        
       
#Content: while-loops, userinput, casting, if and else statements, comparison operators, expression with pow(), boolean value

#Exempel 1

principle = 0 #Beloppet på mitt bankkonto som initials sätt till 0
rate = 0 #Räntan på mitt bankkonto
time = 0 #Tiden i år

while principle <= 0:
    principle = float(input("Enter the principle amount: "))    #casting
    if principle <= 0:
        print("Principle can´t be less than or equal to zero")  #Beloppet måste vara > 0. Om inte körs loppen från början.


while rate <= 0:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("Interest rate can´t be less than or equal to zero")


while time <= 0:
    time = int(input("Enter the time in years: "))  #Omvandlas till heltal eftersom det är hela år
    if time <= 0:
        print("Time can´t be less than or equal to zero")

total = principle * pow((1 + rate / 100), time)   #pow = upphöjt i 
#Formel för att beräkna beloppet på bankkontot när man tagit hänsyn till det ursprungliga beloppet, ränta och antal år
#
print(f"Balance after {time} year/years: ${total:.2f}") #F-strings, två decimaler
print("\n")


#Exempel 2: Om användaren vill kunna ange 0 men inte mindre än 0

principle = 0 #Beloppet på mitt bankkonto som initials sätt till 0
rate = 0 #Räntan på mitt bankkonto
time = 0 #Tiden i 
print("If the user wants to enter zero for the amount, interest rate and time in years...")


while True: #True är ett booleiskt värde som här betyder att loopen kommer att köras så länge villkoret är sant
    principle = float(input("Enter the principle amount: "))   
    if principle < 0:
        print("Principle can´t be less than zero ")
    else:
        break   #Nu är villkoret falskt. Om inte "break" funnits hade man ej kunnat ta sig ur loopen

while True: 
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Rate can´t be less than zero")
    else:
        break   
        
while True:
    time = int(input("Enter the time in years: "))  
    if time < 0:
        print("Time can´t be less than zero")
    else:
        break
total = principle * pow((1 + rate / 100), time)         
print(f"Balance after {time} year/years: ${total:.2f}") 







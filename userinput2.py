# https://www.youtube.com/watch?v=nMCOB8KElwo&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=4
#Covers: input, f-strings, casting, expressions with variables, rounding


items = input("What items would you like to buy? : ")    
price = float(input("What is the price?: "))    #Exempel på casting: anges med decimaler
quantity = int(input("You must buy at least two items to get a discount. How many would you like?: "))
#Exempel på casting: anges med heltal

totalWithoutDiscount = price * quantity #Priset exklusive rabatten
discount = totalWithoutDiscount * 0.3   #Rean är på 30 procent
totalWithDiscount = totalWithoutDiscount - discount #Priset inklusive rabatten

print(f"You have bought {quantity} {items}")
print(f"Your total without discount is ${round(totalWithoutDiscount, 1)}")
print(f"Your total with discount is ${round(totalWithDiscount, 1)}")#Avrundas med två decimaler om det behövs

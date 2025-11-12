# Slicing strings

credit_number = "1234-5678-9012-3456"
last_digits = credit_number[-4:]    #negativ indexering
print(last_digits)  #de fyra sista siffrorna

first_digits = credit_number[:4]    #de fyra första siffrorna, 0 behöver inte anges i början
print(first_digits)

four_numbers1 = credit_number[0:4]  #de fyra första siffrorna
four_numbers2 = credit_number[5:9]
four_numbers3 = credit_number[10:14]
four_numbers4 = credit_number[15:19]

all_numbers = four_numbers1 + four_numbers2 + four_numbers3 + four_numbers4
print(all_numbers)  #kreditkortsnumret utan streck

converted_numbers = credit_number[::-1]
print(f"The creditcard-number in converted order is: {converted_numbers}")

expression = "Oh My God"
abbreviation = expression[::3]  #trean innebär att var tredje tecken skrivs ut
print(abbreviation) #Förkortningen med stora bokstäver
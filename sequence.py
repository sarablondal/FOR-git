# skref 1. setja inn hversu margar tölur eiga að prentast
# skref 2. búa til kassa sem geymir síðustu þrjár tölurnar 
# og nýjustu töluna sem á að prenta, nefna kassa eftir innihaldi
# skref 3. gera for loop sem tekur inn upplysingar ur skrefi 1 
# skref 4. ef tala nr. 1 er ekki með gildi gefa fyrstu þremur gildunum
# gildin 1, 2 og 3.
# skref 4. ef fyrsta talan er stærri en 0 þá prenta út summu síðustu 3 talnanna.
# skref 5. Prenta summu síðustu 3 talna.
# skref 6. Tala 1 tekur gildi tölu 2, tala 2 tekur gildi tölu 3 og tala 3 tekur gildi tölu fjögur.
# skref 7. endurtaka skref 5 n sinnum
n = int(input("Enter the length of the sequence: ")) # Do not change this line
num1 = 0
num2 = 0
num3 = 0
num4 = 0
for i in range(1,n):
    if num1 == 0:
        num1 = 1
        num2 = 2
        num3 = 3
        print(num1)
        print(num2)
        print(num3)
    else:
        num4= num1+num2+num3
        print(num4)
        num1 = num2
        num2 = num3
        num3 = num4

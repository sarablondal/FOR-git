# 1. skref setja inn tölu.
# 2. skref Búa til if setningu þar sem innsett tala þarf að vera 0<= annars gerist ekkert.
# 3. Ef innsett tala er stærri en vistuð stærsta tala þá verður innsett tala að stærstu.
# 4. skref while number =>0 þá endurtaka skref 1 og skref 3
# 5. skref ef innsett tala er minni en 0 prentast stærsta vistaða tala.
max_int = 0
num_int = int(input("Input a number: "))    # Do not change this line
if num_int >= 0:
    max_int = num_int
    while num_int >= 0:
        num_int = int(input("Input a number: "))
        if num_int > max_int:
            max_int = num_int
print("The maximum is", max_int)    # Do not change this line

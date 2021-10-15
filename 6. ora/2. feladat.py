a,b = 2, 4
if a == 4 or b != 4:
    print("nyert")

if a == 4 or b == 4:
    print("majdnem nyert")

number = 0
print("SZám (1-4): ")
input(number)
if number != 2:
    print("vesztett")

elif number == 3:
    print("kis türelmet")

else:
    print("nyert")

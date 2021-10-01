is_number = False

while not is_number:
    try:
        number = int(input("pls give me an int num:"))
        if number % 2 == 0:
            print("Even")
            is_number = True
        else:
            print("Odd")
            is_number = True
    except ValueError:
        print("Not integer num")

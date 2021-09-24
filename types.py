input_data = input("Kérek egy számot:")

try:
    int_number = int(input_data)
    print("A kapott szám 3-szorosa:", 3*int_number)
    print(type(int_number))
    print(type(input_data))
except ValueError:
    print("I/O Hiba!")


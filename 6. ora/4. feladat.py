
lista = []
try:


    asd = 3

    for i in range(asd):
        asd += 1
        num = input("Adjon meg egy számot: ")
        if num != 0:
            lista.append(num)

        else:
            break
except ValueError:
    print("Valami nem jo...")

print(lista)
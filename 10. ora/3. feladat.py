def sorrend(szamok, hossz):

    temp = 0

    for i in range(hossz):
        for j in range(hossz-1):
            if(szamok[i] < szamok[j]):
                temp = szamok[j]
                szamok[j] = szamok[i]
                szamok[i] = temp

    return szamok

print("Adja meg a lista hosszát: ")
hossz = input()

lista = []

for i in range(int(hossz)):
    print(f"Adja meg a lista {i+1}. elemét: ")
    lista[i] = input()


print(sorrend(lista, hossz))


def max(szamok, hanyadik):
    lista = szamok.copy()

    legn = lista[0]
    legidx = 0

    for i in range(len(lista)-1):
        if(lista[i+1] > legn):
            legn = lista[i+1]
            legidx = i+1

    return legn


lista = []

print("Adja meg hogy hányadik legnagyobb kell: ")
hany = input()

print("Adja meg a lista elemeit: ")
adat = input()

while(adat != 'x'):
    print("Adja meg a lista elemeit: ")
    adat = input()

    if adat.isnumeric():
        lista.append(int(adat))

print(lista)

print(max(lista, hany))
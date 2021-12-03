file = open("szavazatok.txt", "r+")

print("1. feladat: A szavazatok.txt beolvasása.")

hossz = 0;

while(file.readline() != ""):
    hossz += 1

print(f"2. feladat: A helyhatósági választáson {hossz} képvisel?jelölt indult.")

file.seek(0)

szavazatok = []



counter = -1;
szavCounter = 0;

for i in range(hossz):
    uncut = (file.readline()).split()

    szavazatok.append(uncut)


print("3. feladat: Adja meg a képvisel? nevét: ")

valasztott = input()

valasztottCut = valasztott.split()

talalt = False

for i in range(hossz):
    if szavazatok[i][2] == valasztottCut[0] and szavazatok[i][3] == valasztottCut[1]:
        talalt = True

        print(f"A képvisel? {szavazatok[i][1]} szavazatot kapott.")

if talalt == False:
    print("Ilyen nev? képvisel?jelölt nem szerepel a nyilvántartásban!")


leadottSzav = 0

for i in range(hossz):
    leadottSzav += int(szavazatok[i][1])

print(f"4. feladat: A választáson {leadottSzav} állampolgár, a jogosultak {((leadottSzav/12345)*100)}%-a vett részt.")

partok = [0, 0, 0, 0, 0]

partokAranya = [[{"GYEP"},{}],[{"HEP"},{}],[{"TISZ"},{}],[{"ZEP"},{}],[{"-"},{}]]


for i in range(hossz):
    if szavazatok[i][4] == "GYEP":
        partok[0] += int(szavazatok[i][1])

    elif szavazatok[i][4] == "HEP":
        partok[1] += int(szavazatok[i][1])

    elif szavazatok[i][4] == "TISZ":
        partok[2] += int(szavazatok[i][1])

    elif szavazatok[i][4] == "ZEP":
        partok[3] += int(szavazatok[i][1])

    elif szavazatok[i][4] == "-":
        partok[4] += int(szavazatok[i][1])


osszesSzav = 0

for i in range(5):
    osszesSzav += partok[i]

for i in range(5):
    partokAranya[i][1] = (partok[i]/osszesSzav)*100


print("5. feladat: A pártokra leadott szavazatok aránya:")
print(f"Gyümölcsev?k Pártja: {partokAranya[0][1]}%")
print(f"Húsev?k Pártja: {partokAranya[1][1]}%")
print(f"Tejivók Szövetsége: {partokAranya[2][1]}%")
print(f"Zöldségev?k Pártja: {partokAranya[3][1]}%")
print(f"Független jelöltek: {partokAranya[4][1]}%")

'''
kepviselok = [[szavazatok[0][2],szavazatok[0][3],szavazatok[0][4]]]

nincsEBene = True


for i in range(hossz):
    nincsEBene = True

    for j in range(len(kepviselok)):
        if szavazatok[i][2] == kepviselok[j][0] and szavazatok[i][3] == kepviselok[j][1]:
            nincsEBene = False

    if(nincsEBene):
        kepviselok.append([szavazatok[i][2],szavazatok[i][3],szavazatok[i][4]])

print(kepviselok)
'''

kepviselok = szavazatok



for i in range(hossz-1):
    for j in range(hossz):
        if(int(kepviselok[i+1][1]) > int(kepviselok[j][1])):
            temp = kepviselok[i+1]
            kepviselok[i+1] = kepviselok[j]
            kepviselok[j] = temp


print("6. feladat: A választáson a legtöbb szavazatot szerzett képvisel?(k):")
for i in range(3):
    print(f"{kepviselok[i][2]} {kepviselok[i][3]} ({kepviselok[i][4]})")


irando = open("kepviselok.txt", "r+")

gyep = True
hep = True
tisz = True
zep = True
fug = True


for i in range(hossz):
    if (gyep and kepviselok[i][4] == "GYEP"):
        irando.write(f"{kepviselok[i][0]} {kepviselok[i][2]} {kepviselok[i][3]} {kepviselok[i][4]}\n")
        irando.newlines
        gyep = False

    if (hep and kepviselok[i][4] == "HEP"):
        irando.write(f"{kepviselok[i][0]} {kepviselok[i][2]} {kepviselok[i][3]} {kepviselok[i][4]}\n")
        irando.newlines
        hep = False

    if (tisz and kepviselok[i][4] == "TISZ"):
        irando.write(f"{kepviselok[i][0]} {kepviselok[i][2]} {kepviselok[i][3]} {kepviselok[i][4]}\n")
        irando.newlines
        tisz = False

    if (zep and kepviselok[i][4] == "ZEP"):
        irando.write(f"{kepviselok[i][0]} {kepviselok[i][2]} {kepviselok[i][3]} {kepviselok[i][4]}\n")
        irando.newlines
        zep = False

    if (fug and kepviselok[i][4] == "-"):
        irando.write(f"{kepviselok[i][0]} {kepviselok[i][2]} {kepviselok[i][3]} független\n")
        fug = False

irando.close()
file.close()




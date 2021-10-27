

#megnyitás
file = open("text.txt", "r+")
print(file.read())
'''
•r: olvasás
•w: írás a korábbi adatok törlésével
•a: írás a korábbi adatok megőrzésével (hozzáfűzés)
•r+: írás és olvasás, nem töröl, fájl elején kezd
•w+: írás és olvasás, töröl, fájl elején kezd 
•a+: írás és olvasás, nem töröl, fájl végén kezd
'''

#fájl bezárása
file.close()

#teljes tartalom beolvasáa
file.read()

#következő 3 számú karakter beolvasása
file.read(3)

#egy sor beolvaása
file.readline()

#beolvasási pozíció
file.tell()

#teljes tartalom beolvasása
file.readlines()

#fájlba írás
file.write("asdasdasdads")

#állomány frissítése
file.flush()


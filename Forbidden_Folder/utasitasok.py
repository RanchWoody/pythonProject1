

igaz = True
masikIgaz = True
asd = "asd"
szoveg = "rzgzbzrgzurg zrguzr asd"



if igaz:
    print("Igaz volt!")
elif masikIgaz:
    print("Így is igaz!")
else:
    print("Úgyis tudod...")

while igaz:
    print("asd")
    igaz = False

for i in [1, 2, 3, 4, 5]:
    print(i)

for asd in szoveg:
    print("a")

for i in range(3):
    print("asd")


try:
    print("Ide jön az utasítás de úgyis tudod...")
except ValueError:
    print("Valami nem jo...")

'''
BaseExceptionA beépített, rendszer szintű kivételek szülőosztálya.
ExceptionMinden nem rendszer szintű kivétel szülőosztálya.
ArithmeticErrorMinden beépített aritmetikai hibajelzés szülőosztálya.
IndexErrorSzekvencia (pl. lista) indexelése a tartományon kívül esik.
NameErrorNem definiált változónév.
OverflowErrorTúlcsordulás nagyon nagy aritmetikai művelet esetében.
SyntaxErrorAz értelmező szintaktikai hibát talált (nem kezelhető).
TypeErrorBeépített operátornak vagy függvénynek helytelen típust adunk át.
ValueErrorA függvény vagy operátor megfelelő típusú, de nem megfelelő értéket kap paraméterként.
ZeroDivisionErrorOsztásnál vagy modulóműveletnél 0 második argumentum.
'''


#bekérés
print(input())

#átalakítások
chr()
float()
int()
str()
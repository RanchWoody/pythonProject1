import random

try:
    speed = input("Adjon meg egy sebességet (km/h): ")
    speed_int = int(speed)
    speed_int *= 0.277777778
    print(speed_int, "m/s")

except ValueError:
    print("I/O Hiba")

lista = []

for i in range(10):
    lista.append(random.randint(1, 100))

paros_lista = []
paratlan_lista = []


for i in range(len(lista)):
    if lista[i] % 2 == 0:
        paros_lista.append(lista[i])

    else:
        paratlan_lista.append(lista[i])

for i in range(len(paros_lista)):
    print(paros_lista[i], "  ")

for i in range(len(paratlan_lista)):
    print(paratlan_lista[i], "  ")


side = []
side_name = "a"
for i in range(3):
    sid = 0
    while side == 0:
        try:
            side = float(input(f"Kérem adja meg a 3szög {side_name} oldalának értékét: "))
            if side > 0:
                if side_name == "a":
                    side_name = "b"
                else:
                    side_name = "c"

                side.append(sid)
            else:
                side = 0
                print("A 3szög oldala csak poz szám lehet")
        except ValueError:
            print("Nem megfelelő az érték.")

if side[0] + side[1] <= side[2] or side[0] + side[2] <= side[1] or side[2] + side[1] <= side[0]:
    k = side[0] + side[1] + side[2]
    b = k/2
    t = (b * (b - side[0]) * (b - side[1]) * (b - side[2])) ** 0.5
    print("3szög ker {} terület: {}".format(k, t))

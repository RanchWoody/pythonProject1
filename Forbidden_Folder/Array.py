

tomb1 = ["asd", "ert", "vbn"]

#hossz
print(len(tomb1))

#tartalmazza e az elemet
print("asd" in tomb1)

#elem indexe
print(tomb1.index("asd"))

#hozzáadás
tomb1.append("ghj")

#két lista egybeolvasztása
tomb2 = ["dfg", "íyx"]
tomb1.extend(tomb2)

#elem behelyezése egy adott helyre
tomb1.insert(2, "nvure")

#listaelem törlése index alapján
del(tomb1[2])

#listaelem törlése érték alapján
tomb1.remove("asd")

#rendezés, abc és növekvő
tomb1.sort()

#visszafelé rendezés
tomb1.sort(reverse=True)

#megfordítása
tomb1.reverse()

#rendezett másolatt
sorted(tomb1)





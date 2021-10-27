

szoveg = "Vitya hol az oltásod?!"


#megszámolja egy adott szövegrész hányszor volt
print(szoveg.count("Vity"))

#utolso karakter -> t/f
print(szoveg.endswith("!"))

#megkeres egy chart vagy egy stringet és megadja az indexét ahonnan kezdődik, de ha nincs ilyen -1-et dob
print(szoveg.find("ty"))

#ugyan az mint a find csak itt exceptiont dob ha nincs
print(szoveg.index("ty"))

#megadja hogy alfanumerikus e azaz csak betű és szám van e benne
print(szoveg.isalnum())

#megadja hogy minden elem betű e
print(szoveg.isalpha())

#megadja hogy minden elem szám e
print(szoveg.isdigit())
print(szoveg.isnumeric())

#összeköt egy string tömböt a megadott jellel
tomb = ("egy", "kettő", "három")
osszekotottSzoveg = "-".join(tomb)
print(osszekotottSzoveg)

#kicserél egy adott szövegrészt
kicserelt = szoveg.replace("Vitya", "Merkel")
print(kicserelt)

#egy szövegrész utolsó előfordulásának indexe
print(szoveg.rfind("olt"))

#szétválasztja egy tombre a szoveget a megadott karakternél
szetvalasztott = szoveg.split(" ")
print(szetvalasztott)

#ellenőrzi hogy a megadott karakterrel kezdődik e
print(szoveg.startswith("Vi"))

#szoveg hosszát adja meg, length
print(len(szoveg))

#Spec karakterek
print("asd \b asd \r asd \n asd \t asd \' asd \" asd \\")






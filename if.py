number = 20
if number < 100:
    print("Ez a szám kisebb mint 100.")
else:
    print("Ez a szám nem kisebb mint 100")

number1 = 3

if number1 % number == 0:
    print(number1, "Osztója.", number)
else:
    if number % number1 == 0:
        print(number, "osztója", number1)
    else:
        print("NEm osztója")

str1 = "alma"

if str1[0] == str1[-1]:
    print("Az első és utolsó kar megegyezik")
else:
    print("Az első és utolsó kar nem egyezik meg")


if number > 0:
    print("poz")
elif number < 0:
    print("neg")
else:
    print("nulllaa")


if str1[0].isupper():
    print("Az első kar nagybetű")
else:
    print("Kisbetű")

str2 = "almafa"

if str1[0:5] == str2[0:5]:
    print("AZ első 5 kar megegyezik")
else:
    print("Nem egyezik az első 5 kar")



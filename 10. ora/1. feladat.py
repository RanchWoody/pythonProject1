

def megtalal():

    print("Kérem adja meg a szöveget: ")
    string = input();

    print("Kérem adja meg a karaktert: ")
    c = input();
    megtalalt = True

    for i in range(len(string)):
        if(string[i] == c):
            return i
            megtalalt = False
            break

    if megtalalt:
        return -1

print(megtalal())

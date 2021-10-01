try:
    raw_input_data = input("Adja meg a hosszt percekben: ")

    sum_of_sec = int(raw_input_data)

    if sum_of_sec < 0:
        print("Nem megfelelő bemenet.")

    elif sum_of_sec == 0:
        print("Most")

    else:
        sec_in_min = 60
        sec_in_hour = 60 * sec_in_min
        sec_in_days = 24 * sec_in_hour
        sec_in_years = 365 * sec_in_days


        years = sum_of_sec // sec_in_years
        sum_of_sec = sum_of_sec - years * sec_in_years

        days = sum_of_sec // sec_in_days
        sum_of_sec = sum_of_sec - days * sec_in_days

        hours = sum_of_sec // sec_in_hour
        sum_of_sec = sum_of_sec - hours * sec_in_hour

        minutes = sum_of_sec // sec_in_min
        seconds = sum_of_sec - minutes * sec_in_min

        number_of_units = 0
        if years > 0:
            number_of_units += 1
        if days > 0:
            number_of_units += 1
        if hours > 0:
            number_of_units += 1
        if minutes > 0:
            number_of_units += 1
        if seconds > 0:
            number_of_units += 1



        out = ""

        if years > 0:
            out += str(years) + "év"
            if years > 1:
                out += "ek"
            if number_of_units > 2:
                out += ", "
            elif number_of_units == 2:
                out += " és "
            number_of_units -= 1
        if days > 0:
            out += str(days) + "nap"
            if days > 1:
                out += "ok"
            if number_of_units > 2:
                out += ", "
            elif number_of_units == 2:
                out += " és "
            number_of_units -= 1
        if hours > 0:
            out += str(hours) + "óra"
            if hours > 1:
                out += "-(k)"
            if number_of_units > 2:
                out += ", "
            elif number_of_units == 2:
                out += " és "
            number_of_units -= 1
        if minutes > 0:
            out += str(minutes) + "perc"
            if minutes > 1:
                out += "ek"
            elif number_of_units == 2:
                out += " és "
            number_of_units -= 1
        if seconds > 0:
            out += str(seconds) + "másodperc"
            if seconds > 1:
                out += "ek"
            elif number_of_units == 2:
                out += " és "
            number_of_units -= 1

        print(out) ## angolul szebb...
except ValueError:
    print("Hibás összeg.")
def kacsanevek(prefixes= "JKLMNOPQ", suffix= "ack") -> str:
    nevek = ""

    for prefix in prefixes:
        nevek += prefix + suffix + ", "

    return nevek


print(kacsanevek())
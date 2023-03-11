while True:
    print(" ")
    a = int(input("Zadejte prvni cislo: "))
    b = int(input("Zadejte druhe cislo: "))

    print("1) plus")
    print("2) minus")
    print("3) krat")
    print("4) deleno")

    selection = input("Vyberte operaci (1 - 4): ")
    selection = int(selection)

    if selection == 1:
        out = a + b
        print("Vyseledek je : {}".format(out))

    elif selection == 2:
        out = a - b
        print("Vyseledek je : {}".format(out))

    elif selection == 3:
        out = a * b
        print("Vyseledek je : {}".format(out))

    elif selection == 4:
        out = a / b
        print("Vyseledek je : {}".format(out))
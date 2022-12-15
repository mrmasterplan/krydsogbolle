
opslag=" XO"

def print_feldt(feldt):
    bogstaver = [opslag[pos] for pos in feldt]

    print("+---+---+---+")
    print(f"| {bogstaver[6]} | {bogstaver[7]} | {bogstaver[8]} |")
    print("+---+---+---+")
    print(f"| {bogstaver[3]} | {bogstaver[4]} | {bogstaver[5]} |")
    print("+---+---+---+")
    print(f"| {bogstaver[0]} | {bogstaver[1]} | {bogstaver[2]} |")
    print("+---+---+---+")

def hvem_vandt(feldt):
    linerne = [
        # vandrete liner
        (0,1,2),
        (3,4,5),
        (6,7,8),
        # skraa liner
        (6,4,2),
        (8,4,0),
        # lodrette liner
        (8,5,2),
        (7,4,1),
        (6,3,0)
    ]
    for line in linerne:
        for vinder in [1,2]:
            pos0, pos1, pos2 = line
            if feldt[pos0] == vinder and feldt[pos1] == vinder and feldt[pos2] == vinder:
                return vinder
    return 0

def main2():
    feldt = [1,0,1,2,2,2,0,0,1,]

    print_feldt(feldt)

def main():
    feldt = [0,]*9
    print_feldt(feldt)
    # hoved sloejfe
    while True:
        for spiller in [1,2]:
            if not feldt.count(0):
                print("Ingen vandt.")
                return
            # få et træk:
            while True:
                fra_spilleren = input(opslag[spiller]+"s tur: ")
                try:
                    traek = int(fra_spilleren)
                except:
                    print("Du skal give et tal fra 1-9. Prøv igen.")
                    continue
                if traek<1 or traek>9:
                    print("Du skal give et tal fra 1-9. Prøv igen.")
                    continue

                traek = traek-1

                if feldt[traek] != 0:
                    print("feldtet er ikke ledigt. Prøv igen.")
                    continue

                break

            # udfør trækket
            feldt[traek] = spiller
            print_feldt(feldt)
            vinder = hvem_vandt(feldt)
            if vinder:
                print(opslag[vinder], "har vundet")
                return


if __name__ == "__main__":
    main()
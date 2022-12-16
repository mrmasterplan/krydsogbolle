
opslag=" XO"
brikker_per_spiller =3
linerne = [
    # vandrete liner
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    # skraa liner
    (7, 5, 3),
    (1, 5, 9),
    # lodrette liner
    (7, 4, 1),
    (8, 5, 2),
    (9, 6, 3)
]

def print_feldt(feldt):
    bogstaver = [opslag[pos] for pos in feldt]

    print("+---+---+---+")
    print(f"| {bogstaver[7]} | {bogstaver[8]} | {bogstaver[9]} |")
    print("+---+---+---+")
    print(f"| {bogstaver[4]} | {bogstaver[5]} | {bogstaver[6]} |")
    print("+---+---+---+")
    print(f"| {bogstaver[1]} | {bogstaver[2]} | {bogstaver[3]} |")
    print("+---+---+---+")

def hvem_vandt(feldt):
    for line in linerne:
        for vinder in [1,2]:
            pos0, pos1, pos2 = line
            if feldt[pos0] == vinder and feldt[pos1] == vinder and feldt[pos2] == vinder:
                return vinder
    return 0

def main2():
    feldt = [1,0,1,2,2,2,0,0,1,]

    print_feldt(feldt)

def traek_fra_spiller(spiller, feldt):
    print(opslag[spiller] + "s tur: ")
    ledige_feldter = [i for i, f in enumerate(feldt) if f == 0 and i>0]
    if feldt.count(spiller) >= brikker_per_spiller:
        spillerens_brikker = [i for i,f in enumerate(feldt) if f == spiller and i>0]
        print("Du skal flytte en brik.")
        while True:
            tastet = input( f"{opslag[spiller]} vælg fra {spillerens_brikker} og til? ")
            try:
                fjern_brik = int(tastet[0])
                traek = int(tastet[1:])
            except:
                continue
            if fjern_brik in spillerens_brikker and traek in ledige_feldter:
                break
        feldt[fjern_brik] = 0
        feldt[traek] = spiller
    else:

        while True:
            fra_spilleren = input(opslag[spiller] + " placere brik: ")
            try:
                traek = int(fra_spilleren)
            except:
                print("Du skal give et tal fra 1-9. Prøv igen.")
                continue
            if traek < 1 or traek > 9:
                print("Du skal give et tal fra 1-9. Prøv igen.")
                continue


            if traek not in ledige_feldter:
                print("feldtet er ikke ledigt. Prøv igen.")
                continue

            break

        feldt[traek] = spiller


def main():
    feldt = [0,]*10
    print_feldt(feldt)
    # hoved sloejfe
    while True:
        for spiller in [1,2]:
            if not feldt.count(0):
                print("Ingen vandt.")
                return
            # udfør trækket
            traek_fra_spiller(spiller, feldt)



            print_feldt(feldt)
            vinder = hvem_vandt(feldt)
            if vinder:
                print(opslag[vinder], "har vundet")
                return


if __name__ == "__main__":
    main()


def unos_intervala(x, y):
    while True:
        try:
            odabir = int(input(f"Unesite broj u intervalu {x}-{y}: "))
            if odabir < x or odabir > y:
                raise Exception("Molim Vas unesite broj unutar intervala!")
        except ValueError:
            print("Molim Vas unesite broj!")
        except Exception as e:
            print(e)
        else:
            return odabir

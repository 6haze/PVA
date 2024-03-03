def nacti_posloupnost_vstupu():
    try:
        posloupnost = list(map(int, input().split()))
        if len(posloupnost) == 0:
            raise ValueError("Prázdná vstupní posloupnost")
        elif len(posloupnost) > 2000:
            raise ValueError("Vstupní posloupnost je příliš dlouhá")
        return posloupnost
    except ValueError as e:
        print("Chyba:", e)
        return None

def najdi_dvojice_se_stejnym_souctem(posloupnost):
    pocet_dvojic = 0
    soucty = {}
    for i in range(len(posloupnost)):
        aktualni_soucet = 0
        for j in range(i, len(posloupnost)):
            aktualni_soucet += posloupnost[j]
            if j > i:  # Zajistit, že délka intervalu je nejméně 2
                if aktualni_soucet not in soucty:
                    soucty[aktualni_soucet] = 1
                else:
                    pocet_dvojic += soucty[aktualni_soucet]
                    soucty[aktualni_soucet] += 1
    return pocet_dvojic

def main():
    print("Zadejte posloupnost čísel:")
    posloupnost = nacti_posloupnost_vstupu()
    if posloupnost is not None:
        pocet_dvojic = najdi_dvojice_se_stejnym_souctem(posloupnost)
        print("Počet dvojic:", pocet_dvojic)

if __name__ == "__main__":
    main()

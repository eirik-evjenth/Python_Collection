'''
    Blandede oppgaver, nr. 5:
    Du skal nå lage ditt eget «tre på rad»-spill.
    Lag først en todimensjonal liste med tre rader og tre kolonner. Du kan fylle lista med mellomrom (" ") eller en annen verdi som du synes er passende. For de to spillerne kan du bruke "x" og "o".
    Deretter skal du lage en løkke som gjentas helt til spillet er ferdig. Løkka skal be brukeren skrive inn rad, kolonne og symbol, og legge til angitt symbol i den todimensjonale lista. Her kan du legge inn en test som sjekker om feltet allerede er brukt.
    Når en bruker har lagt til et symbol, skal spillbrettet skrives ut på en ryddig måte.
    Spillet er ferdig når en av spillerne har tre på rad, eller når hele brettet er fullt.
'''

import random as rnd

def print_brett(brett):
    for rad in brett:
        print(" | ".join(rad))
        print("-" * 13)

def sjekk_vinner(brett, symbol):
    for i in range(4):
        # Sjekk om alle feltene i raden er like
        rad_vinner = True
        for felt in brett[i]:
            if felt != symbol:
                rad_vinner = False
                break
        if rad_vinner:
            return True

        # Sjekk om alle feltene i kolonnen er like
        kol_vinner = True
        for j in range(4):
            if brett[j][i] != symbol:
                kol_vinner = False
                break
        if kol_vinner:
            return True
    # ELLER, for en mer komplisert, men kortere måte å skrive på..    
    # Sjekk rader og kolonner
    # for i in range(4):
    #     if all([felt == symbol for felt in brett[i]]) or all([brett[j][i] == symbol for j in range(3)]):
    #         return True

    # Sjekk diagonaler
    # if all([brett[i][i] == symbol for i in range(3)]) or all([brett[i][2-i] == symbol for i in range(3)]):
    #     return True

    return False

def brett_fullt(brett):
    for rad in brett:
        for felt in rad:
            if felt == " ":
                return False
    return True

# Funksjonen som kjører selve spillet
def tre_pa_rad():
    #brett = [[" " for _ in range(3)] for _ in range(3)]
    # ELLER, for noe som kan være litt lettere å forstå:
    # Opprett en tom liste for brettet
    brett = []

    # Legg til tre rader
    for i in range(4):
        # Opprett en rad med tre tomme felt
        rad = [" ", " ", " "]
        # Legg raden til brettet
        brett.append(rad)


def tre_pa_rad():
    # Opprett brettet, en tom 3x3 liste
    brett = [[" " for _ in range(4)] for _ in range(4)]
    
    spiller = "x"  # Start med spiller "x"
    
    while True:
        print_brett(brett)
        
        # Be spilleren om å velge rad og kolonne
        try:
            rad = int(input(f"Spiller {spiller}, velg rad (0-3): "))
            kol = int(input(f"Spiller {spiller}, velg kolonne (0-3): "))
        except ValueError:
            print("Ugyldig input, skriv et tall mellom 0 og 3.")
            continue

        # Sjekk om rad og kolonne er gyldige og feltet er tomt
        if rad < 0 or rad > 3 or kol < 0 or kol > 3:
            print("Ugyldig rad eller kolonne, prøv igjen.")
            continue
        if brett[rad][kol] != " ":
            print("Feltet er allerede brukt, prøv igjen.")
            continue
        
        # Legg til symbolet på valgt plass
        brett[rad][kol] = spiller
        
        # Sjekk om spilleren har vunnet
        if sjekk_vinner(brett, spiller):
            print_brett(brett)
            print(f"Spiller {spiller} vinner!")
            break
        
        # Sjekk om brettet er fullt (uavgjort)
        if brett_fullt(brett):
            print_brett(brett)
            print("Uavgjort! Brettet er fullt.")
            break
        
        # Bytt spiller
        if spiller == "x":
            spiller = "o"
        else:
            spiller = "x"

# Kjør spillet
tre_pa_rad()
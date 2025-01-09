# Krypteringsordbok der hver bokstav forskyves med to bokstaver
krypter = {
    "a": "c", "b": "d", "c": "e", "d": "f", "e": "g", "f": "h", "g": "i", "h": "j", "i": "k", "j": "l",
    "k": "m", "l": "n", "m": "o", "n": "p", "o": "q", "p": "r", "q": "s", "r": "t", "s": "u", "t": "v",
    "u": "w", "v": "x", "w": "y", "x": "z", "y": "æ", "z": "ø", "æ": "å", "ø": "a", "å": "b"
}

# Funksjon som krypterer tekst ved å bruke krypteringsordboken
def krypter_tekst(tekst):
    kryptert_tekst = ""
    for bokstav in tekst.lower():
        if bokstav in krypter:
            kryptert_tekst += krypter[bokstav]
        else:
            kryptert_tekst += bokstav  # Legger til tegn som ikke er i ordboka (mellomrom, punktum osv.)
    return kryptert_tekst

# Eksempeltekst for kryptering
tekst = input("Skriv inn noe du ønsker å kryptere: ")

# Kryptere teksten
print()
kryptert_tekst = krypter_tekst(tekst)
print("Kryptert tekst:", kryptert_tekst)

# Dekrypteringsordbok som er det motsatte av krypteringsordboken
dekrypter = {v: k for k, v in krypter.items()}

# Funksjon som dekrypterer tekst ved hjelp av dekrypteringsordboken
def dekrypter_tekst(tekst):
    dekryptert_tekst = ""
    for bokstav in tekst.lower():
        if bokstav in dekrypter:
            dekryptert_tekst += dekrypter[bokstav]
        else:
            dekryptert_tekst += bokstav  # Beholder tegn som ikke er i ordboka
    return dekryptert_tekst

# Dekryptere den krypterte teksten

dekryptert_tekst = dekrypter_tekst(kryptert_tekst)
print("Dekryptert tekst:", dekryptert_tekst)
print()
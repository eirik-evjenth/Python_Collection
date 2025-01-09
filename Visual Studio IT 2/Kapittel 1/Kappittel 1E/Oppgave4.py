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
tekst = "hei på deg, å jobbe med kryptering er gøy!"

# Kryptere teksten
kryptert_tekst = krypter_tekst(tekst)
print("Kryptert tekst:", kryptert_tekst)


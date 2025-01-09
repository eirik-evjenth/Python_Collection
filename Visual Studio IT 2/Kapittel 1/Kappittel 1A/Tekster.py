# Oppgave 20

# Distanse = "100 m"
# Hastighet = "300 000 km/s"
# Nepers_Number = "2,718 281 828 459 045"

# Ny_Distanse = Distanse.replace(" m", "")
# Nyere_Distanse = int(Ny_Distanse) + 100
# print(Nyere_Distanse)

# Hastighetere = Hastighet[:-4]
# Hastigheterere = Hastighetere.replace(" ", "")
# print(Hastigheterere)

# Eiriks_number = Nepers_Number.replace(" ", "").replace(",", "")
# print(Eiriks_number)

# Oppgave 21

ord = "spiser"
lengde = len(ord)
nyttOrd = ord[2] + ord[lengde - 3] # ord[2] tar ut indeks 2, og ord[lengde-3] tar ut indeks -3
print(nyttOrd)
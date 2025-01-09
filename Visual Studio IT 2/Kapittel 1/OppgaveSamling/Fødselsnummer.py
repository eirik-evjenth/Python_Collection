Måneder = {
    "Januar": 1,
    "Februar": 2,
    "Mars": 3,
    "April": 4,
    "Mai": 5,
    "Juni": 6,
    "Juli": 7,
    "August": 8,
    "September": 9,
    "Oktober": 10,
    "November": 11,
    "Desember": 12
}

fødselsnummer = input("Skriv inn fødselsnummeret ditt (11 siffer): ")

if len(fødselsnummer) != 11:
    print("Ugyldig valg")
    exit(1)

dag = fødselsnummer[:2]
måned = fødselsnummer[2:4]
år = fødselsnummer[4:6]

dag = int(dag)
måned = int(måned)

if dag > 31 or dag < 1:
    print("Det må være en ekte dag")
    exit(1)
elif måned > 12 or måned < 1:
    print("Det må være en ekte måned")
    exit(1)

individnummer = int(fødselsnummer[6:9])
if 500 <= individnummer <= 999:
    århundre = "20"
else:
    århundre = "19"

fullt_år = århundre + år

if individnummer % 2 == 1:
    kjønn = "mann"
else:
    kjønn = "kvinne"

for månedsnavn, månedsnummer in Måneder.items():
    if månedsnummer == måned:
        måned = månedsnavn
        break

if int(fullt_år) > 2024:
    print("Dette året har ikke skjedd enda")
    exit(1)

elif måned == "April" or måned == "Juni" or måned == "September" or måned == "November" and dag > 30:
    print("Antall dager i måneden tilsvarer ikke måneden du skrev inn")
    exit(1)
elif måned == "Februar" and dag > 28:
    print("Antall dager i måneden tilsvarer ikke måneden du skrev inn")
    exit(1)


print(f"Fødselsdatoen din er: {dag}.{måned}.{fullt_år} og du er en {kjønn}")


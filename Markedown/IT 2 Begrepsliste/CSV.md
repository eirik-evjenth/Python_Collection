# CSV

- CSV-filer er filer som inneholder rader med data, hver rad representerer en post. 
- Det er en separator som komma, semikolon eller tabulator (\t) som er brukt for å skille de forskjellige radene. 
- Fordeler med CSV er at det er lett å lese/skrive av mennesker og programmer. Det er også gjenkjent av de fleste programmeringsspråk, databaser og regneark som Excel. 
- Lite overhead sammenlignet med andre datafil formater som JSON eller XML.

## Lesing av CSV eksempel:

```python
import csv

with open('filenavn.csv', 'r') as fil:
    reader = csv.reader(fil)
    for rad in reader:
        print(rad)
```

## Skriving til CSV eksempel:

```python
import csv

with open('ny_fil.csv', 'w',newline='' as fil:
    writer = csv.writer(fil)
    writer.writerow(['Navn', 'Alder', 'By'])
    writer.writerow(['Ola', 18, 'Oslo'])
```

## Bruk av pandas som mer avansert metode

```python
import pandas as pd

# lesing
df = pd.read_csv('filenavn.csv')
print(df)

# Skriving
df.to_csv('utdata.csv', index=False)
```

## Formateringsutfordringer med CSV filer

- Spesialtegn som anførselstegn eller linjeskift må håndteres selv.
- Sjekk hvilket delimiter-format som brukes i csv fil, endres fra Europa til USA.
- Når det er manglende data (tomme celler) som NaN (Not a number) eller None må man håndtere det.

## Relevans for IT 2

### a) Integrasjon med databaser
- CSV-filer brukes ofte til å importere eller eksportere data til databaser (som MySQL eller SQLite).
- Bruk SQL til å hente, manipulere og eksportere data til CSV.

### b) Filbehandling
- CSV-filer kan brukes som en del av programmering for å:
    - Hente data til programmet.
    - Prosessere informasjon (som lønnslister, resultater eller kundedata).
    - Laste opp data til webapplikasjoner eller analysere dem i backend.

### c) Automatisering
- Automatisere databehandling ved å kombinere skript og CSV-filer, f.eks. for å generere rapporter.

### d) Dataanalyse
- CSV-filer brukes til å analysere og visualisere data, som er nyttig i mange IT-prosjekter.

## Tips for bruk av CSV:

- Sjekk at dataen i CSV-filen er korrekt før det behandles, evt vask dataen slik at det er ingen problemer.
- Bruk try-catch blokker for å håndtere feil ved lesing eller skriving
- riktig tegnsett for å unngå problemer med spesialtegn (UTF-8 encoding)
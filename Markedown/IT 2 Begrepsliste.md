# IT 2 begrepsliste

## CSV

- CSV-filer er filer som inneholder rader med data, hver rad representerer en post. 
- Det er en separator som komma, semikolon eller tabulator (\t) som er brukt for å skille de forskjellige radene. 
- Fordeler med CSV er at det er lett å lese/skrive av mennesker og programmer. Det er også gjenkjent av de fleste programmeringsspråk, databaser og regneark som Excel. 
- Lite overhead sammenlignet med andre datafil formater som JSON eller XML.

### Lesing av CSV eksempel:

```python
import csv

with open('filenavn.csv', 'r') as fil:
    reader = csv.reader(fil)
    for rad in reader:
        print(rad)
```

### Skriving til CSV eksempel:

```python
import csv

with open('ny_fil.csv', 'w',newline='' as fil:
    writer = csv.writer(fil)
    writer.writerow(['Navn', 'Alder', 'By'])
    writer.writerow(['Ola', 18, 'Oslo'])
```

### Bruk av pandas som mer avansert metode

```python
import pandas as pd

# lesing
df = pd.read_csv('filenavn.csv')
print(df)

# Skriving
df.to_csv('utdata.csv', index=False)
```

### Formateringsutfordringer med CSV filer

- Spesialtegn som anførselstegn eller linjeskift må håndteres selv.
- Sjekk hvilket delimiter-format som brukes i csv fil, endres fra Europa til USA.
- Når det er manglende data (tomme celler) som NaN (Not a number) eller None må man håndtere det.

### Relevans for IT 2

#### a) Integrasjon med databaser
- CSV-filer brukes ofte til å importere eller eksportere data til databaser (som MySQL eller SQLite).
- Bruk SQL til å hente, manipulere og eksportere data til CSV.

#### b) Filbehandling
- CSV-filer kan brukes som en del av programmering for å:
    - Hente data til programmet.
    - Prosessere informasjon (som lønnslister, resultater eller kundedata).
    - Laste opp data til webapplikasjoner eller analysere dem i backend.

#### c) Automatisering
- Automatisere databehandling ved å kombinere skript og CSV-filer, f.eks. for å generere rapporter.

#### d) Dataanalyse
- CSV-filer brukes til å analysere og visualisere data, som er nyttig i mange IT-prosjekter.

### Tips for bruk av CSV:

- Sjekk at dataen i CSV-filen er korrekt før det behandles, evt vask dataen slik at det er ingen problemer.
- Bruk try-catch blokker for å håndtere feil ved lesing eller skriving
- riktig tegnsett for å unngå problemer med spesialtegn (UTF-8 encoding)


## HTTP-requests

HTTP-requests (HyperText Transfer Protocal) er grunnlaget for kommunikasjon på internett. Det brukes for å hente data og sende data mellom klienter (nettlesere eller applikasjoner) og servere

### Hva er en HTTP-request?

HTTP-requests er forespørsler sendt fra en klient til en server. Klienten ber om data (en nettside eller API-data) og serveren svarer med en respons.

### Viktigste HTTP-metodene:

For å håndtere HTTP-metoder bruker vi Flasj, som er et lettvekts rammeverk for Python som brukes til å bygge webapplikasjoner og API-er. Her er hvordan metodene fungerer i Flask og hvordan du kan bruke dem i praksis

#### Opprett en enkel Flask-app:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Velkommen til Flask-appen!"

if __name__ == '__main__':
    app.run(debug=True)
```
Dette oppretter en server som svarer på forespørsler på URL-en `http://127.0.0.1:5000/`

I flask kan du spesifisere hvilket HTTP-metoder en rute skal håndtere ved å bruke `methods`-parameteret i `@app.route`.

#### a) GET

- Brukes for å hente (to get) data fra en server.
- Når en nettside åpnes sendes en GET-forespørsel.
- Standard metode hvis `methods` ikke er spesifisert:

```python
@app.route('/hent_data', methods=['GET'])
def hent_data():
    return {"melding": "Her er data fra serveren!"}
```

#### b) POST
- brukes til å sende data til serveren, ofte gjennom forespørselens kropp:
```python
from flask import request

@app.route('/send_data', methods=['POST'])
def send_data():
    data = request.json  # Henter JSON-data fra forespørselen
    return {"mottatt": data}
```

#### c) PUT
- brukes til å oppdatere eksisterende data:
```python
@app.route('/oppdater_data/<int:id>', methods=['PUT'])
def oppdater_data(id):
    data = request.json
    return {"id": id, "oppdatert_data": data}
```

#### d) DELETE
- Brukes til å slette ressurser.
```python
@app.route('/slett_data/<int:id>', methods=['DELETE'])
def slett_data(id):
    return {"melding": f"Ressurs med id {id} er slettet"}
```

### Håndtering av data

#### a) Query Parameters

brukes til å sende data via URL-en.

- Eksempel-URL: `/søk?navn=Eirik`
- håndtering i Flask:
```python
@app.route('/søk', methods=['GET'])
def søk():
    navn = request.args.get('navn')
    return {"søkt_etter": navn}
```

#### b) Form Data

Data sendt via skjema (oftest fra en nettisde):
```python
@app.route('/skjema', methods=['POST'])
def skjema():
    data = request.form
    return {"skjema_data": data}
```

#### c) JSON-data
- Data sendes i JSON-format (vanlig for API-er).
```python
@app.route('/json', methods=['POST'])
def json_data():
    data = request.json
    return {"mottatt_json": data}
```

### Bruk av HTTP-statuskoder

Du kan spesifisere statuskoder i Flask-responser:
```python
@app.route('/feil')
def feil():
    return {"feil": "Noe gikk galt"}, 400  # 400 Bad Request
```

### Flere funksjoner i Flask:

#### a) RESTful API

Bygg RESTful API-er ved å bruke HTTP-metoder til å håndtere CRUD.operasjoner:
```python
from flask import jsonify

data = []

@app.route('/ressurs', methods=['POST'])
def opprett_ressurs():
    ny_data = request.json
    data.append(ny_data)
    return {"melding": "Ressurs opprettet"}, 201

@app.route('/ressurs/<int:id>', methods=['GET'])
def hent_ressurs(id):
    if id < len(data):
        return jsonify(data[id])
    return {"feil": "Ressurs ikke funnet"}, 404

@app.route('/ressurs/<int:id>', methods=['PUT'])
def oppdater_ressurs(id):
    if id < len(data):
        data[id] = request.json
        return {"melding": "Ressurs oppdatert"}
    return {"feil": "Ressurs ikke funnet"}, 404

@app.route('/ressurs/<int:id>', methods=['DELETE'])
def slett_ressurs(id):
    if id < len(data):
        data.pop(id)
        return {"melding": "Ressurs slettet"}
    return {"feil": "Ressurs ikke funnet"}, 404
```

#### b) Middleware

Flask lar deg legge til mellomliggende funksjoner (middleware) for logging, autentisering, osv.
```python
@app.before_request
def før_hver_forespørsel():
    print("En ny forespørsel er mottatt!")

@app.after_request
def etter_hver_respons(response):
    print("Respons sendt!")
    return response
```

### Debugging og Testing

- Bruk `debug=True` i `app.run` for å se feilmeldinger og automatiske laste inn endringer.

## Anonyme funksjoner (Lambda) i Python

Lambda-funksjoner brukes for å lage små navnløse (anonyme) funksjoner. Nyttig for korte operasjoner som ikke trenger en definisjon med `def`.

### Grunnleggende syntaks
En lambda-funksjon er definert med nøkkelordet `lambda` etterfulgt av:
1. Argument(er)
2. En enkel uttrykk
3. Lamda returnerer alltid verdien av uttrykket
```python
lambda argument1, argument2: uttrykk
```
Eksempel:
```python
# En funksjon som legger sammen to tall
addisjon = lambda x, y: x + y
print(addisjon(3, 5)) # Output: 8
```

### Når bruker man lambda-funksjoner?

- Når du trenger en liten funksjon èn gang, uten å navngi den.
- Typiske bruksområder: `map()`, `filter()`, `sorted()`, og `reduce()`

### Eksempler

#### 1. Med innebygde funksjoner

#### a) `map()`

`map()` brukes til å bruke en funksjon på alle lementene i en iterervar (f.eks. liste):
```python
# Bruk lambda til å kvadrere alle tall i en liste
tall = [1, 2, 3, 4]
kvadrat = list(map(lambda x: x**2, tall))
print(kvadrat) # output: [1, 4, 9, 16]
```

#### b) `filter()`

`filter()` brukes til å filtrere elementer fra en itererbar basert på en betingelse:
```python
# Filter ut tall som er større enn 2
tall = [1,2,3,4]
større_enn_to = list(filter(lambda x: x>2, tall))
print(større_enn_to) # Output: [3,4]
```

#### c) `sorted()`

`sorted()` kan sortere basert på en nøkkelfunksjon.
```python
# Sorter en liste av tupler etter andre element
data = [(1,3),(2,2),(4,1)]
sortert = sorted(data, key=lambda x: x[1])
print(sortert) # Output [(4,1),(2,2),(1,3)]
```

#### 2. som inline-funksjoner

I stedet for å definere en funksjon med `def`, kan lambda funksjon brukes direkte:
```python
# Vanlig funksjon
def kvadrat(x):
    return x ** 2

# Med lamda
lambda_kvadrat = lambda x: x ** 2
print(lambda_kvadrat(5)) # Output: 25
```

### Begrensinger av lambda-funksjoner

1. Lambda-funksjoner kan bare inneholde ett enkelt uttrykk, og ikke ha flere linjer.
2. Brukes oftest for enkel logikk og kan bli uleselig hvis de blir for komplekse.

### Tips med anonyme funksjoner (Lambda)

- Bruk lambda der det gir mening, men hvis funksjonaliteten blir for kompleks, bør banlig strategi med `def` bli brukt for bedre lesbarhet
- Lambda kan integreres med rammeverk som Flask for enkel databehandling i webapplikasjoner.


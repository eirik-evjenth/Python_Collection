# HTTP-requests

HTTP-requests (HyperText Transfer Protocal) er grunnlaget for kommunikasjon på internett. Det brukes for å hente data og sende data mellom klienter (nettlesere eller applikasjoner) og servere

## Hva er en HTTP-request?

HTTP-requests er forespørsler sendt fra en klient til en server. Klienten ber om data (en nettside eller API-data) og serveren svarer med en respons.

## Viktigste HTTP-metodene:

For å håndtere HTTP-metoder bruker vi Flask, som er et lettvekts rammeverk for Python som brukes til å bygge webapplikasjoner og API-er. Her er hvordan metodene fungerer i Flask og hvordan du kan bruke dem i praksis

### Opprett en enkel Flask-app:

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

### a) GET

- Brukes for å hente (to get) data fra en server.
- Når en nettside åpnes sendes en GET-forespørsel.
- Standard metode hvis `methods` ikke er spesifisert:

```python
@app.route('/hent_data', methods=['GET'])
def hent_data():
    return {"melding": "Her er data fra serveren!"}
```

### b) POST
- brukes til å sende data til serveren, ofte gjennom forespørselens kropp:
```python
from flask import request

@app.route('/send_data', methods=['POST'])
def send_data():
    data = request.json  # Henter JSON-data fra forespørselen
    return {"mottatt": data}
```

### c) PUT
- brukes til å oppdatere eksisterende data:
```python
@app.route('/oppdater_data/<int:id>', methods=['PUT'])
def oppdater_data(id):
    data = request.json
    return {"id": id, "oppdatert_data": data}
```

### d) DELETE
- Brukes til å slette ressurser.
```python
@app.route('/slett_data/<int:id>', methods=['DELETE'])
def slett_data(id):
    return {"melding": f"Ressurs med id {id} er slettet"}
```

## Håndtering av data

### a) Query Parameters

brukes til å sende data via URL-en.

- Eksempel-URL: `/søk?navn=Eirik`
- håndtering i Flask:
```python
@app.route('/søk', methods=['GET'])
def søk():
    navn = request.args.get('navn')
    return {"søkt_etter": navn}
```

### b) Form Data

Data sendt via skjema (oftest fra en nettisde):
```python
@app.route('/skjema', methods=['POST'])
def skjema():
    data = request.form
    return {"skjema_data": data}
```

### c) JSON-data
- Data sendes i JSON-format (vanlig for API-er).
```python
@app.route('/json', methods=['POST'])
def json_data():
    data = request.json
    return {"mottatt_json": data}
```

## Bruk av HTTP-statuskoder

Du kan spesifisere statuskoder i Flask-responser:
```python
@app.route('/feil')
def feil():
    return {"feil": "Noe gikk galt"}, 400  # 400 Bad Request
```

## Flere funksjoner i Flask:

### a) RESTful API

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

### b) Middleware

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

## Debugging og Testing

- Bruk `debug=True` i `app.run` for å se feilmeldinger og automatiske laste inn endringer.

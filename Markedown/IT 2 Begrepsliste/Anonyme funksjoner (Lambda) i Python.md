# Anonyme funksjoner (Lambda) i Python

Lambda-funksjoner brukes for å lage små navnløse (anonyme) funksjoner. Nyttig for korte operasjoner som ikke trenger en definisjon med `def`.

## Grunnleggende syntaks
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

## Når bruker man lambda-funksjoner?

- Når du trenger en liten funksjon èn gang, uten å navngi den.
- Typiske bruksområder: `map()`, `filter()`, `sorted()`, og `reduce()`

## Eksempler

### 1. Med innebygde funksjoner

### a) `map()`

`map()` brukes til å bruke en funksjon på alle lementene i en iterervar (f.eks. liste):
```python
# Bruk lambda til å kvadrere alle tall i en liste
tall = [1, 2, 3, 4]
kvadrat = list(map(lambda x: x**2, tall))
print(kvadrat) # output: [1, 4, 9, 16]
```

### b) `filter()`

`filter()` brukes til å filtrere elementer fra en itererbar basert på en betingelse:
```python
# Filter ut tall som er større enn 2
tall = [1,2,3,4]
større_enn_to = list(filter(lambda x: x>2, tall))
print(større_enn_to) # Output: [3,4]
```

### c) `sorted()`

`sorted()` kan sortere basert på en nøkkelfunksjon.
```python
# Sorter en liste av tupler etter andre element
data = [(1,3),(2,2),(4,1)]
sortert = sorted(data, key=lambda x: x[1])
print(sortert) # Output [(4,1),(2,2),(1,3)]
```

### 2. som inline-funksjoner

I stedet for å definere en funksjon med `def`, kan lambda funksjon brukes direkte:
```python
# Vanlig funksjon
def kvadrat(x):
    return x ** 2

# Med lamda
lambda_kvadrat = lambda x: x ** 2
print(lambda_kvadrat(5)) # Output: 25
```

## Begrensinger av lambda-funksjoner

1. Lambda-funksjoner kan bare inneholde ett enkelt uttrykk, og ikke ha flere linjer.
2. Brukes oftest for enkel logikk og kan bli uleselig hvis de blir for komplekse.

## Tips med anonyme funksjoner (Lambda)

- Bruk lambda der det gir mening, men hvis funksjonaliteten blir for kompleks, bør banlig strategi med `def` bli brukt for bedre lesbarhet
- Lambda kan integreres med rammeverk som Flask for enkel databehandling i webapplikasjoner.
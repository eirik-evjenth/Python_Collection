# Valgoperatør (Ternary Operator)

Valgoperatøren (ofte kalt en ternary operator) er en kompakt måte å skrive en betinget uttrykk på, som en enkel erstatning for en if-else-struktur. Den brukes til å evaluere en betingelse og velge mellom to verdier basert på om betingelsen er sann eller usann

## Syntaks

```python
verdi1 if betingelse else verdi2
```
- `betingelse`: Dette er en boolsk uttrykk som avalueres til `True` eller `False`.
- `verdi1`: Returneres hvis betingelsen er sann.
- `verdi2`: Returneres hvis betingelsen er usann.

## Eksempler

### 1. Grunnleggende bruk
```python
alder = 18
melding = "Myndig" if alder >= 18 else "Ikke mynding"
print(melding) # Output: Myndig
```

### 2. Innrede betingelser

Man kan bruke valgoperatøren som et alternativ til mer ekplisitte `if-else`-blokker:
```python
tall = 5
paritet = "Partall" if tall % 2 == 0 else "Oddetall"
print(paritet) # Output: Oddetall
```

### 3. Med funksjoner

Du kan bruke valgoperatlren i funksjoner for å gjøre koden mer kompakt
```python
def sjekk_positiv(antall):
    return "Positiv" if antall > 0 else "Negativ eller null"

print(sjekk_positive(3)) # Output: Positiv
print(sjekk_positive(-1)) # Output: Negativ eller null
```

## Fordeler

1. Reduserer antall linjer og gjør koden mer kompakt/oversiktlig.
2. Bedre lesbarhet for enkle betingelser
3. Veldig fleksibel bruksområder (I funksjoner, listeforståelser, og returnuttalelser)

## Begrensinger

- Hvis uttrykket blir for komplekst kan det være vanskelig å lese
```python
# Eksempel på dårlig lesbarhet:
melding = "Premium" if bruker["poeng"] > 100 else "Standard" if bruker["poeng"] > 50 else "Basic"
```
Det er bedre å bruke en vanlig `if-else`for komplekse strukturer.
- Valgoperatøren kan ikke strekke seg over flere linjer.
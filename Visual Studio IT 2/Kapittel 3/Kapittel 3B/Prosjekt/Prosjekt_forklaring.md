# Prosjektforklaring

Dette prosjektet handler om å analysere aksjekursen til NVIDIA og Apple, litt sammenligning med S&P 500. Anbefaler å lese om Apple først, siden jeg går mer grundig i visse emner. Har skrevet om planene mine fra starten, loggen min for hva jeg har gjort (ekskluderer mye jeg gjorde utenfor timene), også selve analysene.

## Litt om bibliotekene

```python
from datetime import datetime
import matplotlib.pyplot as plt
import csv
from matplotlib.ticker import FuncFormatter
import pandas as pd
```

Dette er bibliotekene jeg har tatt i bruk og som trengs for å kjøre kodene.
- Datetime var brukt for å gjøre om tider til datoer og omvendt. 
- Matplotlib.pyplot brukte jeg for å plotte dataen
- csv brukte jeg for å lese av CSV filene
- matplotlib.ticker sin funksjon "FuncFormatter" for å formatere store numre om til noe mer lesbar, 
eks 1e6 = 1 M(illion)
- pandas ble brukt for å analysere dataen lettere.

## Datainnsamling
For å analysere NVIDIA og Apple sine aksjekurser har jeg brukt ulike datakilder. NVIDIA-dataen ble hentet fra Kaggle-datasettet [Stock Market Data](https://www.kaggle.com/datasets/paultimothymooney/stock-market-data). Dette datasettet inneholder mye historisk informasjon, men er ikke oppdatert til de nyeste kursene. For mer oppdatert data om Apple og S&P 500 brukte jeg `yfinance`, et bibliotek som henter sanntids aksjeinformasjon fra Yahoo Finance. Jeg brukte følgende kode for å laste ned data:


```python
import yfinance as yf

data = yf.download("AAPL", start="1980-12-12", end="2025-02-13")
spy_data = yf.download('SPY', start='1980-12-12', end='2025-02-13')

spy_data.to_csv("S&P 500.csv")
data.to_csv("AAPL_max.csv")
```


I tillegg brukte jeg Investopedia for å forstå og forklare økonomiske begreper knyttet til aksjemarkedet, inflasjon og volatilitet.

## Begrepsliste:

Brukte Investopedia for det meste, her er noen definisjoner:

- Aksjekurs – Prisen på en enkelt aksje i et selskap, bestemt av tilbud og etterspørsel.
- Volatilitet – Hvor mye en aksjekurs svinger over tid; høy volatilitet betyr store prisendringer.
- Dot-com-boblen – En spekulativ bølge på slutten av 1990-tallet hvor teknologiaksjer steg raskt og krasjet.
- Finanskrisen 2008 – En global økonomisk krise forårsaket av sammenbruddet i boligmarkedet og banksektoren.
- Kryptovaluta – Digital valuta basert på blokkjedeteknologi, som Bitcoin og Ethereum.
- NFT (Non-Fungible Token) – En unik digital eiendel lagret på en blokkjedeteknologi.
- Inflasjon – Økning i prisnivået over tid, som reduserer pengeverdien.
- S&P 500 – En aksjeindeks som måler de 500 største selskapene i USA.
- YFinance – Et Python-bibliotek for å hente finansdata fra Yahoo Finance.
- Likviditet – Hvor enkelt en eiendel kan kjøpes eller selges i markedet uten store prisendringer.
- Markedsverdi – Totalt aksjeverdi for et selskap, beregnet som aksjekurs * antall aksjer.
- DeepSeek – En avansert KI-modell som har påvirket aksjeverdien til NVIDIA negativt.
- Helgehandel – Aksjemarkedet er stengt i helgene, så det er ingen handel lørdag og søndag.
- Markedsandel – Den prosentvise andelen et selskap har av det totale markedet innen sin bransje, ofte brukt for å måle konkurranseevne.


## Analyse og utfordringer
En viktig faktor i analysen er inflasjon. Det er vanskelig å måle inflasjon på verdensbasis, dette gjorde at jeg kunne ikke justere for inflasjon og måtte bare se på dollar verdien over tid. Derfor er noen av de største endringene ikke justert og mindre i aktualitet. Mesteparten av analysen er USA-basert, siden det er markedet jeg har mest kjennskap til. Derfor bruker jeg S&P 500 som en referanseindeks for å sammenligne aksjene med markedets generelle utvikling.

En utfordring i tillegg til inflasjon er med at aksjedata ikke finnes i helgene, siden det er ingen handel de dagene (aksjee markedet er sntengt). Alle aksjer har derfor manglende data på lørdager og søndager, noe som er viktig å ta hensyn til ved trendanalyser.

## NVIDIA og AI
Navnet NVIDIA kommer fra det latinske ordet for "misunnelse" og akronymet NV, som står for "next vision". NVIDIA har hatt en eksplosiv vekst de siste årene, spesielt grunnet utviklingen innen kunstig intelligens. AI-modeller krever enorm regnekraft, og NVIDIA sine GPU-er har blitt essensielle for trening av store språkmodeller og dyp læring. Dette er hvorfor jeg bestemte å analysere de.

NVIDIA har hatt stor vektst i de årene etter dataen jeg analyserte. Dette er grunnet den explosive veksten av KI (kunstig intelligens). ChatGPT har vært den største, og de bruker NVIDIA sine GPU-er for å få mer compute og utvikle KI-en raskere.

I slutten av januar 2025 opplevde NVIDIA en betydelig nedgang i aksjekursen etter lanseringen av DeepSeek, en kinesisk AI-modell som ble lagd både billigere og mer effektiv enn eksisterende løsninger. Denne nyheten utløste bekymringer blant investorer om at etterspørselen etter NVIDIAs avanserte AI-brikker kunne avta, noe som resulterte i et aksjefall på 17 % og et verdifall på rundt 600 milliarder dollar (Størst noensinne). 

Til tross for den umiddelbare negative reaksjonen, har NVIDIAs administrerende direktør (CEO), Jensen Huang, uttalt at DeepSeeks fremskritt faktisk kan øke behovet for selskapets maskinvare. Han påpeker at mer avanserte AI-modeller krever betydelig datakraft, noe som kan styrke etterspørselen etter NVIDIAs produkter (NVIDIA hoppet tilbake etter det). 

Videre har store teknologiselskaper som Amazon og Meta økt sine investeringer i AI-infrastruktur, noe som indikerer en fortsatt sterk etterspørsel etter NVIDIAs løsninger. 



## Apple og navnets opprinnelse
Apple sitt navn stammer fra Steve Jobs sin "fascinasjon" for epler. Ifølge [Macworld](https://www.macworld.com/article/673923/why-is-apple-called-apple.html) valgte han navnet fordi han likte epler, og fordi det hørtes vennlig og ikke-teknisk ut sammenlignet med konkurrentene på den tiden.

## Konklusjon
Dette prosjektet har gitt innsikt i hvordan aksjemarkedet reagerer på teknologiske trender, inflasjon og økonomiske svingninger. Ved å analysere NVIDIA og Apple har jeg sett hvordan innovasjon innen AI og historiske hendelser har påvirket aksjekursene. Til tross for databegrensninger, gir analysene et tydelig bilde av markedets utvikling. Jeg har prøvd å gi kilder der jeg har brukt, men mye generell kunnskap har jeg fått av å lese mye om markedet og finans.
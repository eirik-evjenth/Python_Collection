# Kryptering og Kryptografiske Algoritmer

Kryptering er prosessen med å sikre data ved å gjøre den uleselig for uautoriserte personer. Dette skjer ved å bruke en algoritme og en nøkkel for å transformere informasjonen til en uleselig form (kalt "ciphertext"). For å hente tilbake originaldataen ("plaintext") fra krypteringen, må man ha tilgang til den riktige nøkkelen eller passordet. Her er grunnleggende forklaring på noen vanlige krypteringsmetoder:

## AES (Advanced Encryption Standard)

- Symmetrisk krypteringsalgoritme, som betyr den bruker samme nøkkel både for kryptering og dekryptering
- AES er veldig rask og trygg, og brukes til å beskytte alt fra filsystemer til kommunikasjon på internett
- AES kan bruke ulike nøkkelstørrelser: 128, 192, eller 256 biter. Jo lengre nøkkel desto mer sikker er krypteringen, men det kan også gjøre krypteringen litt tregere (som er fordelen med AES).

## RSA (Rivest-Shamir-Adleman)

RSA er en asymmetrisk krypteringsalgoritme, som betyr at den bruker et par med nøkler: en offentlig nøkkel og en privat nøkkel. Den offentlige nøkkelen brukes til å kryptere data, men det private nøkkelen brukes for å dekryptere dem. Dette gjør RSA ideel for situasjoner der man trenger å sende sikre data til noen uten å ha delt en hemmelig nøkkel på forhånd (som i tilfelle med AES).

- RSA brukes ofte til å kryptere små mengder data, som for eksempel å sende nøkler for symmetrisk kryptering.

## SHA (Secure Hash Algorithm)

SHA er en hash-funksjon og brukes for å lage en "fingeravtrykk" (eller sammenfatning) av data. Dette er ike egentlig kryptering, fordi det ikke finnes en vei tilbake til originaldataene. Sha-algoritmer (som SHA.256) tar inn data av vilkårlig størrelse og gir en fast lengde (f.eks. 256 biter for SHA-256). SHA brukes i mange sammengenger som å lage digitale signaturer, sjekke integritet (verifisere at data ikke er blitt endret) og lagre passord på en sikker måte.

- Hashing er en enveiskryptering, og kan ikke reverseres for å få tilbake originaldataen.
- SHA er populært brukt i digitale signaturer, blokkjedeteknologie (som Bitcoin), og autentisering.
navn = "Pål"
karakterer = [3, 4, 6, 6, 5, 4]

karaktertekst = ""
for i in range(len(karakterer)):
  
  if len(karakterer) - i < 2:
    karaktertekst += " og "
  elif i > 0:
    karaktertekst += ", " 
  karaktertekst += str(karakterer[i])

print(f"{navn} fikk karakterene {karaktertekst}")
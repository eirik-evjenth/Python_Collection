import json

filnavn = "Json files\Eksempel.json"

with open(filnavn, encoding="utf-8") as fil:
    data = json.load(fil)

# Find and print the genres of "To Kill a Mockingbird"
for book in data["books"]:
    if book["title"] == "To Kill a Mockingbird":
        print(book["genres"][0])
        break
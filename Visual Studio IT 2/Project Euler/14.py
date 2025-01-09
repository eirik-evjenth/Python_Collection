import random

def generate_spanish_text():
    subjects = ["El gato", "La niña", "El perro", "El hombre", "La mujer"]
    verbs = ["come", "bebe", "corre", "salta", "duerme"]
    objects = ["la comida", "el agua", "en el parque", "la cuerda", "en la cama"]

    subject = random.choice(subjects)
    verb = random.choice(verbs)
    object = random.choice(objects)

    sentence = f"{subject} {verb} {object}."
    return sentence

if __name__ == "__main__":
    print(generate_spanish_text())
    def generate_spanish_text():
        subjects = ["El gato", "La niña", "El perro", "El hombre", "La mujer"]
        verbs = ["come", "bebe", "corre", "salta", "duerme", "lee", "escribe", "habla", "escucha", "mira"]
        objects = ["la comida", "el agua", "en el parque", "la cuerda", "en la cama", "un libro", "una carta", "con su amigo", "una canción", "la televisión"]
        prepositions = ["en", "con", "sobre", "bajo", "entre", "hacia", "desde", "sin", "por", "para"]

        subject = random.choice(subjects)
        verb = random.choice(verbs)
        object = random.choice(objects)
        preposition = random.choice(prepositions)

        sentence = f"{subject} {verb} {preposition} {object}."
        return sentence

    if __name__ == "__main__":
        for _ in range(10):
            print(generate_spanish_text())
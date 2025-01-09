def portrait_or_landscape():

    høyde = int(input("Hvor mange piksler høyt er bildet?: "))
    bredde = int(input("Hvor mange piksler bred er bildet?: "))

    if høyde == bredde:
        return print("Det er en firkant")
    elif høyde > bredde:
        return print("Det er en Portrait")
    else:
        return print("Det er en Landscape")
    
portrait_or_landscape()
def billet_pris(alder):
    if 6 <= alder <= 17:
        return 63
    elif 18 <= alder <= 66:
        return 157
    elif alder > 66:
        return 79
    else:
        return 0
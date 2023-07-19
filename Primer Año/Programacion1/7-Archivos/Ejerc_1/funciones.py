def calculoEdad(nac):
    aH = 2023
    mH = 6
    dH = 3
    aD, aM, aA = nac.split("/")
    edad = aH - int(aA)
    if int(aM) > mH or int(aM) == mH and int(aD) > dH:
        edad -= 1
    return edad

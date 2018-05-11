import string


def translate(s):
    eredmeny = []
    szavak = s.split(" ")
    for index, szo in enumerate(szavak):
        ujszo = ""
        szo = szo.strip(string.punctuation) 
        ##----------------

        if len(szo) > 1:
            if index == 0:
                ujszo = ujszo + szo[1].upper()
            else:
                ujszo = ujszo + szo[1].lower()

            ujszo = ujszo + szo[2:] + szo[0].lower() + "ay"
        else:
            ujszo = ujszo + szo[0].lower() + "ay"

        eredmeny.append(ujszo)

    return " ".join(eredmeny) + "." 


def backTranslate(s):
    eredmeny = []
    szavak = s.split(" ")
    for index, szo in enumerate(szavak):
        ujszo = ""
        szo = szo.strip(string.punctuation)
        # -------
        szo = szo[:-2]     # leszedve "ay" végződést

        if index == 0:
            ujszo = ujszo + szo[len(szo)-1].upper() 
        else:
            ujszo = ujszo + szo[len(szo)-1]

        ujszo = ujszo + szo[:-1].lower()

        eredmeny.append(ujszo)

    return " ".join(eredmeny) + "."

#.........MAIN...........

print(translate("The. quick, brown? fox_ e"))
print(backTranslate("Hetay uickqay rownbay oxfay eay."))

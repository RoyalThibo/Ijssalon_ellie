from algemene_functies import mijn_functie_2



def aanbieding_1(smaak, prijs, korting):
    nieuwe_prijs = prijs * (1 - korting)
    uitvoer = f"Vandaag in de aanbieding: Emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {nieuwe_prijs} euro."
    return uitvoer

smaak = "aardbei"

print(aanbieding_1("aardbei", 4, 0.1))

def inkomsten_totaal(inkomsten, btw):
    totaal_inkomsten = sum(inkomsten)
    btw_bedrag = totaal_inkomsten * 0.09
    totaal_btw = btw_bedrag + totaal_inkomsten
    btw_los = totaal_btw - totaal_inkomsten
    uitvoer_btw = f"Het totaal van alle inkomsten van deze week is {totaal_inkomsten} euro, waarover {btw_los} euro btw betaald dient te worden."
    return uitvoer_btw

inkomsten = [220, 430, 125, 160, 205, 90, 345]
print(inkomsten_totaal(inkomsten, 0.09))

#Deze functie is niet herbruikbaar 
def laag_hoog():
    mijn_lijst = [220, 430, 125, 160, 205, 90, 345]
    hoog = max(mijn_lijst)
    laag = min(mijn_lijst)
    print(hoog, laag)

print (laag_hoog())

def gemiddelde(mijn_lijst):
    totaal = sum(mijn_lijst)
    aantal = len(mijn_lijst)
    gemiddelde_bedrag = totaal / aantal
    return f"De gemiddelde inkomsten van deze week zijn {gemiddelde_bedrag} euro."


mijn_lijst = [220, 430, 125, 160, 205, 90, 345]
print(gemiddelde(mijn_lijst))

def laag_hoog2(mijn_lijst):
    hoog = max(mijn_lijst)
    laag = min(mijn_lijst)
    return[hoog, laag]


def meervoudig(invoer_lijst):
    return laag_hoog2(invoer_lijst)

invoer_lijst = [10,5,3,2,1,2,9]
print(meervoudig(invoer_lijst))

def combinatie(invoer_lijst_2):
korte_lijst = laag_hoog2(invoer_lijst_2)
uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
return uitvoer

    


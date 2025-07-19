mijn_dictionary = {
    "aardbei" : "3",
    "vanille" : "4",
    "chocolade" : "5",
}
aanbieding = (3 * 0.8)

reclame_tekst = f"vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {aanbieding}"
reclame_tekst2 = reclame_tekst[:63]
reclame_tekst3 = (reclame_tekst2).upper()
reclame_tekst4 = (reclame_tekst3).split(" ")


#print(aanbieding)
#print(reclame_tekst)
#print(reclame_tekst2)
#print(reclame_tekst3)
print(reclame_tekst4)

el = reclame_tekst4
for item in el:
    if len(item) > 5:
        print(item.upper())
    else:
        print(item.lower())
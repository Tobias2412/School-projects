def validate_tekst(text):
    if '@' in text and len(text) >= 5:
        return True
    else:
        return False

tekst1 = "Tobias@"
tekst2 = "Tobi"
tekst3 = "Tobias@gsfdgfdg"
tekst4 = "Tobiasgsgfgdf"

resultat1 = validate_tekst(tekst1)
resultat2 = validate_tekst(tekst2)
resultat3 = validate_tekst(tekst3)
resultat4 = validate_tekst(tekst4)

print("Resultat for tekst1:", resultat1)
print("Resultat for tekst2:", resultat2)
print("Resultat for tekst3:", resultat3)
print("Resultat for tekst4:", resultat4)

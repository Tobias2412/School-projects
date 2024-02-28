drikkevarer = [
    {'navn': 'Kakao', 'pris': 15},
    {'navn': 'Kaffe', 'pris': 10},
    {'navn': 'Te', 'pris': 12},
    {'navn': 'Cappucino', 'pris': 20}
]
def vaelg_drik():
    print("Vælg en varm drik:")
    for i in range(len(drikkevarer)):
        print(f"{i + 1}. {drikkevarer[i]['navn']} ({drikkevarer[i]['pris']} DKK)")

    valg = int(input("Indtast nummeret på din valgte drik: "))
    return drikkevarer[valg - 1]


def server_drik(valgt_drik):
    print(f"Din {valgt_drik['navn']} serveres. Nyd din drik!")
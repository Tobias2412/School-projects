navne = ["Anna", "Bo", "Pia", "Jesper", "Anders", "Torben"]

total_laengde_paa_navne = 0

for x in navne:
    total_laengde_paa_navne += len(x)

print(total_laengde_paa_navne)
print(total_laengde_paa_navne/len(navne))
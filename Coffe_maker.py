import Coffee_module

while True:
    print("Vil du betale med kort?")
    betalingsmetode = input("Indtast 'kort' for at betale med kort: ").lower()

    if betalingsmetode == 'kort':
        valgt_drik = Modul1.vaelg_drik()
        Modul1.server_drik(valgt_drik)
        print("Tak for dit køb!")
        break


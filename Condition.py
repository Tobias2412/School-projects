def inbetween_numbers(lav, hoej, andet):
    if lav < andet < hoej:
        print(f"Tallet {andet} er imellem {lav} og {hoej}")
    elif andet > hoej:
        print(f"Tallet {andet} er stoerre end {hoej}")
    elif andet < lav:
        print(f"Tallet {andet} er mindre end {lav}")
    else:
        print(f"Tallet {andet} er lig med et af de to: {lav}, {hoej}")


inbetween_numbers(int(input("Lavt nummer: ")), int(input("Heojt nummer: ")), int(input("Andet nummer: ")))
summe = 0

for feld in range(64):
        reiskorn = 2**feld
        summe = summe + reiskorn
        gewicht = summe * 0.03 / 1000 / 1000
        print("Feld {} = {:>30,} Reiskörner und insgesamt {:>30,}".format(feld+1, reiskorn, summe))
print()
print("Bei einem Gewicht von 0,02 Gramm pro Korn wiegen alle Körner zusammen")
print("{:,.0f} Tonnen".format(gewicht))
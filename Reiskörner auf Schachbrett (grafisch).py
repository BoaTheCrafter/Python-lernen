import matplotlib.pyplot as plt
summe = 0
felderListe = []

for feld in range(64):
        reiskorn = 2**feld
        felderListe.append(reiskorn)
        summe += reiskorn
        gewicht = summe * 0.03 / 1000 / 1000

        print(f"Feld {feld+1} = {reiskorn:>30,} Reiskörner und insgesamt {summe:>30,} Reiskörner")

print()
print("Bei einem Gewicht von 0,02 Gramm pro Korn wiegen alle Körner zusammen")
print("{:,.0f} Tonnen".format(gewicht))

plt.plot(felderListe)
plt.show()
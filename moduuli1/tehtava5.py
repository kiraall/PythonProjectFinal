import math
leiviskät, naulat, luodit = float(input("Anna leiviskät: ")), float(input("Anna naulat: ")), float(input("Anna luodit: "))

luoti_grammoina = 13.3
naula_grammoina = 32 * luoti_grammoina
leiviska_grammoina = 20 * naula_grammoina

kokonaisgrammat = (
    leiviskät * leiviska_grammoina +
    naulat * naula_grammoina +
    luodit * luoti_grammoina
)

kilogrammat = (kokonaisgrammat / 1000)
grammat = kokonaisgrammat % 1000

print(f"{kilogrammat} kilogrammaa ja {grammat:.2f} grammaa.")


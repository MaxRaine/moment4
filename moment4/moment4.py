
import random as rnd

sluta = int(input("Hur många loops vill du köra?"))

while True:
    f = input("Vill du göra en ny beräkning? Ja eller Nej")

    if f == "ja":

        x = int(input("Ange Långa sidan"))

        y = int(input("Ange korta sidan"))

        area=x*y

        print(area)

        for i in range(1,10):
            volume = i*area
            print(f"Rektangen {i} har volymen {volume} ")

    elif f == "nej":
        break


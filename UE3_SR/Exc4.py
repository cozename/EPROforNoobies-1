import random 
dice1 = random.randint(1,20)
dice2 = random.randint(1,20)


if dice1 > dice2:
    max = dice1
else:
    max = dice2


if max == 20:
    print("Kritischer Treffer!")
else:
    print(f"Normaler Treffer: {max}")
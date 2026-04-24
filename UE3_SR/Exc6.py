import math

People      = int(input("People: "))
Possibility = 1 - math.factorial(365) / (365**People * math.factorial(365 - People))
print(f"{Possibility * 100:.2f}%")

People = 1
Possibility = 0
while Possibility < 0.5:
    Possibility = 1 - math.factorial(365) / (365**People * math.factorial(365 - People))
    People = People + 1

print(f"In a room of {People - 1} , there is a >50% chance of two people sharing a birthday.")
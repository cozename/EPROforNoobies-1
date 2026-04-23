n = int(input("Jahr: "))
if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
    print("Schaltjahr JA")
else:
    print("Schaltjahr NEIN")
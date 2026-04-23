n = int(input("n: "))
m = int(input("m: "))

if m > n:
    # n ist kleiner
    if m % n == 0:
        print("n ist ein Teiler von m")
    else:
        print("n ist kein Teiler von m")

elif n > m:
    # m ist kleiner
    if n % m == 0:
        print("m ist ein Teiler von n")
    else:
        print("m ist kein Teiler von n")

elif n == m:
    print("n und m sind gleich - jede Zahl ist Teiler von sich selbst")
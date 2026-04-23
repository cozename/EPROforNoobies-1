n = int(input("n: "))
line1 = "0 " * n
line2 = " " + "0 " * n
print((line1 + "\n" + line2 + "\n") * (n//2))
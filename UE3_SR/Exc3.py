n = int(input("n: "))
s = ""

if n % 3 == 0:
    s = s + "Fizz"
if n % 5 == 0:
    s = s + "Buzz"

print(s or "error")
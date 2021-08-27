n = 1

while (n := n + 1) <= 100:
    if (n % 3) == 0:
        print(n, "Fizz")

    if (n % 5) == 0:
        print(n, "Buzz")

    if (n % 3) == 0 and (n % 5) == 0:
        print(n,"Fizz Buzz")

    if (n%3)!=0 and (n%5) !=0:
        print(n)
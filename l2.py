n1 = int(input("first number"))
n2 = int(input("second number"))
result = 0

if n1 > n2:
    result = n1 - n2
    print(result)
elif n1 < n2:
    result = n1 + n2
    print(result)
elif n1 == n2:
    result = n1 * n2
    print(result)
    
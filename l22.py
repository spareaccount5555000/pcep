n1 = int(input("year"))

if n1 % 400 == 0 or (n1 % 4 == 0 and n1 % 100 != 0):
    print("leap year")
else:
    print("not leap year")

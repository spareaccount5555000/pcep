income = float(input("income"))
tax = 0

if income <= 85528:
    tax = income*0.18 - 556.02
    if tax < 0:
        tax = 0
else:
    tax = (income - 85528)*0.32 + 14839.02

print(int(tax))

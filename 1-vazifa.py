from decimal import Decimal

def todecimal(n):
    return Decimal(n)

n=float(input('Float son kiriting\n=>'))
print(todecimal(n))
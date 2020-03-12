price = int(input())
priceCoupon = input()
if priceCoupon == 'Cash3000':
    price -= 3000
elif priceCoupon == 'Cash5000':
    price -= 5000
print(price)
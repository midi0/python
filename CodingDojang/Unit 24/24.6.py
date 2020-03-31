a = map(int, input().split(';'))
prices = list(a)
prices.sort(reverse=True)
count = 0
for i in prices:
    print('%9s' %format(prices[count], ','))
    count += 1
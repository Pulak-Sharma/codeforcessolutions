n = int(input())
denominations = [100, 20, 10, 5, 1]
count = 0
for denom in denominations:
    count += n // denom
    n %= denom
print(count)
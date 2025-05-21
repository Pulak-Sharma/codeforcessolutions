y = int(input())
while True:
    y = y + 1
    if len(set(str(y)))==4:
        break
print(y)
n = int(input())
tram = 0
max = 0
for i in range(n):
    a,b = (int(j) for j in input().split())
    tram -= a
    tram += b
    if tram > max:
        max = tram
print(max)
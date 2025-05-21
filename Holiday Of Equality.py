n = int(input())
a = list(map(int, input().split()))
burles = 0
max = max(a)
for i in a:
    burles += max - i
print(burles)
num = list(map(int, input().split()))
num.sort()
a = num[3] - num[0]
b = num[3] - num[1]
c = num[3] - num[2]
print(a,b,c)
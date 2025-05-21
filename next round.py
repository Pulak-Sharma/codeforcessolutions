n,k = map(int, input().split())
t = 0
a = list(map(int, input().split()))
for i in range(n):
    if a[i]>=a[k] and a[i]!=0:
        t+=1

print(t)

n,h = map(int, input().split())
a = list(map(int, input().split()))
width = n
for i in range(0,n):
    if a[i]>h:
        width+=1
print(width)
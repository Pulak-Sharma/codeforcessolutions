n = int(input())
output = 0
for _ in range(n):
    p,q = map(int, input().split())
    if q-p>=2:
        output+=1
print(output)
n = int(input())
output = 0
for i in range(n):
    sol = list(map(int, input().split()))
    if sum(sol)>=2:
        output+=1
print(output)
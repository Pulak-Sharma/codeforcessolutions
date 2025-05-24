n = int(input())
p = list(map(int, input().split()))
min_score = max_score = p[0]
output = 0
for i in range(1, n):
    if p[i] > max_score:
        output += 1
        max_score = p[i]
    elif p[i] < min_score:
        output += 1
        min_score = p[i]
print(output)
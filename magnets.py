n = int(input())
m1 = input()
groups = 1
for i in range(n-1):
    m = input()
    if m1!=m:
        m1 = m
        groups+=1
print(groups)
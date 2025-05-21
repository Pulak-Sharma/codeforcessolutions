'''t = int(input())
for _ in range(t):
    d = list(map(str, input().split()))
    d.sort()
print(d)'''

t = int(input())
output = ''
for _ in range(t):
    ahead = 0
    a,b,c,d = map(int, input().split())
    if b>a:
        ahead+=1
    if c>a:
        ahead+=1
    if d>a:
        ahead+=1
    output+=f'{ahead}\n'
print(output)
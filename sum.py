t = int(input())
output = ''
for i in range(t):
    a,b,c = map(int, input().split())
    if max(a,b,c)==((a+b+c)-max(a,b,c)):
        output+='YES\n'
    else:
        output+='NO\n'
print(output)
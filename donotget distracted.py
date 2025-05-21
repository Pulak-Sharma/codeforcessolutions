'''t = int(input())
output = ''
for _ in range(t):
    l = int(input())
    s = input()
    if sorted(s)==s or len(set(s))==len(s):
        output+='YES'
    else:
        output+='NO'
print(output)'''

t = int(input())
output = []
for _ in range(t):
    l = int(input())
    s = input()
    distracted = False
    for i in range(l - 1):
        if s[i] != s[i + 1] and s[i] in s[i + 1:]:
            distracted = True
            break
    if distracted:
        output.append('NO')
    else:
        output.append('YES')
print('\n'.join(output))
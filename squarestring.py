t = int(input())
output=''
for i in range(t):
    s = input()
    mid = len(s) // 2 
    if s[:mid]==s[mid: ]:
        output+='YES\n'
    else:
        output+='NO\n'
print(output)
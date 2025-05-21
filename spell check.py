t = int(input())
output = ''
for _ in range(t):
    n = int(input())
    s = input()
    if len(s) == 5 and 'T' in s and 'i' in s and 'm' in s and 'u' in s and 'r' in s:
        output+="YES\n"
    else:
        output+="NO\n"
print(output)

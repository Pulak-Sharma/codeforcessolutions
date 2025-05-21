s = input()
upper = 0
lower = 0
for i in range(0,len(s)):
    if 65<=ord(s[i])<=90:
        upper += 1
    elif 97<=ord(s[i])<=122:
        lower += 1
if upper<=lower:
    print(s.lower())
elif upper>lower:
    print(s.upper())
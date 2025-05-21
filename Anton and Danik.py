n = int(input())
s = input()
anton = 0
for i in range(0,len(s)):
    if s[i]=='A':
        anton+=1
if anton>(len(s)-anton):
    print("Anton")
elif anton==(len(s)-anton):
    print("Friendship")
else:
    print("Danik")
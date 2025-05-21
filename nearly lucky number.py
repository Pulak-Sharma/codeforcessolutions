n = input()
lucky = 0
for i in range(0,len(n)):
    if n[i]=='4' or n[i]=='7':
        lucky += 1
if lucky==4 or lucky==7:
    print("YES")
else:
    print("NO")

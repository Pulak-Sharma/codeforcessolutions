n = int(input())
stones = input()
output = 0
for i in range(n-1):
    if stones[i]==stones[i+1]:
        output+=1
print(output)
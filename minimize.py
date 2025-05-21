output = ''
for _ in range(int(input())):
    a,b = map(int, input().split())
    output+=str(b-a)+'\n'
print(output)
n = int(input())
output = ''
for i in range(n):
    s = input()
    if len(s)>10:
        t = s[0]+str(len(s)-2)+s[len(s)-1]
        output+= f'{t}\n'
    else:
        output+=f'{s}\n'
print(output)


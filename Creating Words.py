output = ''
for _ in range(int(input())):
    a,b = map(str, input().split())
    t = a[0]
    a = b[0] + a[1:]
    b = t + b[1:]
    output+= (a + ' ' + b + '\n')
print(output)
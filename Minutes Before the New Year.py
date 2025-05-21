t = int(input())
output = ''
for _ in range(t):
    minutes = 0
    h,m = map(int, input().split())
    minutes = 1440 - (60*h + m)
    output+=str(minutes)+'\n'
print(output)
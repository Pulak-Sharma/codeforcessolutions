t = int(input())
output = ''
for _ in range(t):
    x,y,n = map(int, input().split())
    for k in range(n,-1,-1):
        if k%x==y:
            output+=str(k)+'\n'
            break
print(output)

'''
t = int(input())
output = ''
for _ in range(t):
    x, y, n = map(int, input().split())
    k = n - (n - y) % x  # Calculate the largest k such that k % x == y
    if k <= n:
        output += str(k) + '\n'
    else:
        output += str(k - x) + '\n'
print(output)

'''
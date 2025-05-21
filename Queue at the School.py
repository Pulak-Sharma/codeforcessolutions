'''n,t = map(int, input().split())
s = input()
for _ in range(t):
    for i in range(len(s)):'''


#solution
n, time = map(int,input().split())
q = list(input())

swapped = False
for t in range(time):
    i = 0
    while (i<n-1):
        if q[i] == 'B' and q[i+1] == 'G':
            q[i],q[i+1] = q[i+1] , q[i]
            swapped = True
            i +=2
        else : i += 1
    if not swapped :
        break

output = ""
print(output.join(q))
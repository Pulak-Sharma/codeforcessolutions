'''m,n = map(int, input().split())
output = ''
for _ in range(1,m+1):
    if m%2!=0:
        output+='#'*n + '\n'
    elif m%2==0:
        output+='.'*(n-1)+'#'+'\n'
print(output)'''

n, m = map(int, input().split())
for i in range(1, n+1):
    if i==1:
        print("#"*m)
        continue
    elif i %2 == 0 and (i % 4) != 0:
        print("."*(m-1)+"#")
        continue
    elif i % 2 != 0:
        print("#"*m)
        continue
    elif i % 4 == 0:
        print("#"+"."*(m-1))
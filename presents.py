n = int(input())
s = list(map(int, input().split()))
for i in range(1,n+1):
    print(s.index(i)+1, end=' ')
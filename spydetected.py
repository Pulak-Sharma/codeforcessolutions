for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))

    for i in range(n):
        if s.count(s[i])==1:
            print(i+1)
            break

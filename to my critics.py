for _ in range(int(input())):
    num = list(map(int, input().split()))
    num = sorted(num)  
    if num[1] + num[2] >= 10:
        print("YES")
    else:
        print("NO")
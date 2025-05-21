for _ in range(int(input())):
    n = int(input())
    count = 0
    while n>1:
        n=n//4
        count+=1
    print(2**count)
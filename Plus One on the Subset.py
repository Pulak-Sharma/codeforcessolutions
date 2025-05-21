for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    moves = max(a)-min(a)
    print(moves)
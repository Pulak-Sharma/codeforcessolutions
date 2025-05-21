for _ in range(int(input())):
    n = int(input())
    s = input()
    moves = 0
    if s.count('1')==0:
        print('0')
    else:
        for i in range(1,n):
            if s[i]!=s[i-1]:
                moves+=1
        print(moves+1)
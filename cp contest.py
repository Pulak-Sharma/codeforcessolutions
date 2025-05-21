s = ""
for _ in range(int(input())):
    n = int(input())
    for i in range(n):
        notes = input()
        for u in range(len(notes)):
            if notes[u] == "#":
                s+= str(u+1) 
                break
print(s)

r1,r2 = map(int, input().split())
c1,c2 = map(int, input().split())
a1,a2,b1,b2 = 0


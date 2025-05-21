m_score = 0
c_score = 0
for _ in range(int(input())):
    m,c = map(int, input().split())
    if m>c:
        m_score+=1
    elif c>m:
        c_score+=1
if m_score>c_score:
    print("Mishka")
elif c_score>m_score:
    print("Chris")
else:
    print("Friendship is magic!^^")
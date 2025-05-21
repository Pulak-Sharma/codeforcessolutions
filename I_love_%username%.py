n = int(input())
score = list(map(int, input().split()))
output = 0
for i in range(len(score)):
    for j in  range(0,i):
        if score[i]>score[j]:
            output+=1
    if score[i]==min(score):
        output+=1
print(output)


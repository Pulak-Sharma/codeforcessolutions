n,k = map(int, input().split())
problem_time = 0
problems = 0
for i in range(1,n+1):
    problem_time += 5*i
    if 240-k>=problem_time:
        problems+=1
print(problems)

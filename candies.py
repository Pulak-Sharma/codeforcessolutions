t = int(input())
outputstr = []
for _ in range(t):
    a= 0
    b= 0
    output = 0
    n = int(input())
    for i in range(1,n):
        a = n-i
        b = i
        if a!=b and a>b:
            output+=1
    outputstr.append(str(output)) 
print('\n'.join(outputstr))

#To reduce the time complexity of your code, you can simplify the logic to count the number of valid pairs (a, b) such that a + b = n and a > b. Here's the optimized version:


t = int(input())
outputstr = []
for _ in range(t):
    n = int(input())
    output = (n - 1) // 2
    outputstr.append(str(output))
print('\n'.join(outputstr))


#Removed unnecessary initializations of a and b.
#Simplified the logic to directly calculate the number of valid pairs using the formula (n - 1) // 2.







'''t = int(input())
outputstr = []
for i in range(t):
    a,b = map(int, input().split())
    if a % b == 0:
        output = 0
    else:
        output = b - (a % b)
    outputstr.append(str(output))   
print('\n'.join(outputstr))'''
def is_prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input())
for i in range(1,int(n/2)+1):
    if not is_prime(i):
        continue
    for j in range(i,int(n/2)+1):
        if not is_prime(j):
            continue
        if i+j==n:
            print(i,j)

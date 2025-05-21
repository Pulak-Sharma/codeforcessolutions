'''n,m = map(int, input().split())
prime = [n]
for i in range(n+1, m+1):
    if m%i==0:
        prime.append(i)

if prime.index(m)==prime.index(n)+1:
    print("YES")
else:
    print("NO")'''
    

def is_prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n, m = map(int, input().split())

next_prime = n + 1
while not is_prime(next_prime):
    next_prime += 1

# Check if the next prime is m
if next_prime == m:
    print("YES")
else:
    print("NO")
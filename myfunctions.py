def is_prime(n):
    divisors = 0
    for i in range(2,n+1):
        if n%i==0:
            divisors+=1
    if divisors==1:
        return True
    else:
        return False
    
def fibonacci(n):
    first = 0
    second = 1
    result = []
    for i in range(n):
        result.append(first)
        first, second = second, first + second
    return result

print(fibonacci(8))
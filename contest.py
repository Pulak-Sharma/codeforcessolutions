for _ in range(int(input())):
    n, m, l, r = map(int, input().split())
    shift = (n - m) // 2
    l_prime = l + shift
    r_prime = l_prime + m
    print(l_prime, r_prime)
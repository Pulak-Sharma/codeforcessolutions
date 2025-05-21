no_of_terms = 0
for _ in range(int(input())):
    n = int(input())
    round_numbers = []
    place = 1
    while n > 0:
        digit = n % 10
        if digit != 0:
            round_numbers.append(digit * place)
            no_of_terms +=1
        n //= 10
        place *= 10
    print(len(round_numbers))
    print(' '.join(map(str, round_numbers)))

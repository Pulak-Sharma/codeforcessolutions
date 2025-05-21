for _ in range(int(input())):
    m,k = map(int, input().split())
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))
    l1 = sorted(l1)
    '''l2 = sorted(l2)
    if sum(l1)>sum(l2):
        for i in range(k):
            l1[i]=l2[-(i+1)]
        num=sum(l1)
    elif sum(l2)>sum(l1):
        for i in range(k):
            l2[i]=l1[-(i+1)]
        num=sum(l2),sum(l1)
    print(num)'''

    l2 = sorted(l2, reverse=True)  # Sort l2 in descending order for easier swapping

    for i in range(min(k, m)):  # Ensure we don't exceed the length of the lists
        if l1[i] < l2[i]:  # Only swap if it increases the sum of l1
            l1[i], l2[i] = l2[i], l1[i]
        else:
            break  # Stop swapping if no further improvement is possible

    print(max(sum(l2),sum(l1)))  # Print the sum of the modified l1 for each test case
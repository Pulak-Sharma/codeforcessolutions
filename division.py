t = int(input())
output = ''
for i in range(t):
    rating = int(input())
    if rating <= 1399:
        output+='Division 4\n'
    elif 1400<=rating<=1599:
        output+='Division 3\n'
    elif 1600<=rating<=1899:
        output+='Division 2\n'
    elif 1900<=rating:
        output+='Division 1\n'
print(output)
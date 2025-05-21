n = int(input())
faces = 0
for _ in range(n):
    hedron = input().lower()
    if 'tetra' in hedron:
        faces+=4
    elif 'octa' in hedron:
        faces+=8
    elif 'dodeca' in hedron:
        faces+=12
    elif 'icosa' in hedron:
        faces+=20
    elif hedron=='cube':
        faces+=6
print(faces)

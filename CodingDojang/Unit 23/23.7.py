col, row = map(int,input().split(' '))
matrix = []
for i in range(row):
    matrix.append(list(input()))

for i in range(row):
    for j in range(col):
        if matrix[i][j] == "*":
            print(matrix[i][j], sep='', end='')
        else:
            count = 0
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    if x < 0 or y < 0 or x >= row or y >= col:
                        continue

                    elif matrix[x][y] == "*":
                        count += 1
            print(count, sep='', end='')

    print()
'''
for i in range(row):
    for j in range(col):
        if matrix[i][j] == '*':
            continue
        else:
            matrix[i][j] = 0
            for y in range(i-1, i+2):
                for x in range(j-1, j+2):
                    if y < 0 or x < 0 or y >= row or x >= col:
                        continue
                    elif matrix[x][y] == '*':
                        matrix[i][j] += 1
            print(matrix[x][])
for i in range(col):
    for j in range(row):
        print(matrix[i][j], sep='', end='')
    print()
'''
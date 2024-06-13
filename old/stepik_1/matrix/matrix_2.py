def input_matrix(n, m):
    matrix = []
    for i in range(n):
        temp = []
        for j in range(m):  
            temp.append(input())
        matrix.append(temp)
    return matrix

def print_matrix(matrix, n, m, width=1):
    for r in range(n):
        for c in range(m):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()

def print_matrix_rev(matrix, n, m, width=1):
    for c in range(m):
        for r in range(n):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()

n, m = int(input()), int(input())

matrix = input_matrix(n, m)
print_matrix(matrix, n, m)
print()
print_matrix_rev(matrix, n, m)



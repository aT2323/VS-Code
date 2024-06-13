def matrix_square(n):
    matrix = []
    for i in range(n):
        temp = [int(num) for num in input().split()]
        matrix.append(temp)
    return matrix

def out_track(matrix):
    track = 0
    for i in range(len(matrix)):
        track += matrix[i][i]
    return track

n = int(input())

matrix = matrix_square(n)
print(out_track(matrix))
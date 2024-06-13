def matrix_square(n):
    matrix = []
    average = []
    for i in range(n):
        temp = [int(num) for num in input().split()]
        matrix.append(temp)
        average.append(sum(temp)/n)

    return matrix, average

def out_count(matrix):
    for i in range(len(matrix)):
        count = 0
        for j in range(len(matrix)):
            if matrix[i][j] > average[i]:
                count +=1
        print(count)

n = int(input())

matrix, average  = matrix_square(n)
out_count(matrix)
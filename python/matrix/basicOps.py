matrix = [[ i for i in range(4)] for j in range(7)]

print(f"matrix")
for r in range(len(matrix)):
    print(matrix[r])

#print(f"matrix {matrix}")

matrix_mirror = [[matrix[i][j] for j in range(len(matrix[0])-1,-1,-1)] for i in range(0,len(matrix))]

print(f"\nmatrix_mirror")
for r in range(len(matrix_mirror)):
    print(matrix_mirror[r])


matrix_transpose = [[  matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0])) ]

#matrix_transpose = [[  (j,i) for j in range(len(matrix))] for i in range(len(matrix[0])) ]

print(f"\nmatrix_transpose")
for r in range(len(matrix_transpose)):
    print(matrix_transpose[r])


matrix_transpose_mirror = [[  matrix[j][i] for j in range(len(matrix)-1,-1,-1)] for i in range(len(matrix[0])-1,-1,-1) ]

#matrix_transpose = [[  (j,i) for j in range(len(matrix))] for i in range(len(matrix[0])) ]

print(f"\nmatrix_transpose")
for r in range(len(matrix_transpose_mirror)):
    print(matrix_transpose_mirror[r])
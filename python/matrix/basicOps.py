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

#spiral matrix columns left to right, rows top to bottom, cols left to right, rows bottom up
# col count len(m[0]) row count = len(m) -2
# col range 0 - len(m[0]), len(m[0])-1, 0
# row range 0+1 - len(m)-1 , len(m)-1-1, 0
# every loop increase and decrease start and end for row and col values
# within each iteration check if start and end are within limits

#total rounds = no of rows/2 or (+1) if %2 is 1


matrix = [[ i for i in range(7)] for j in range(1)]

min_of_cols_rows = min(len(matrix),len(matrix[0]))
no_of_spirals = min_of_cols_rows//2 if min_of_cols_rows%2 == 0 else min_of_cols_rows//2 + 1


# row = 0 , len(matrix)-1-row
# ci = 0
# cj = len(matrix[0]) -1
#
# col = len(matrix[0]) -1,  len(matrix[0]) -1 -1
# ri = 1
# rj = len(matrix) -2


row_no = 0
col_s = 0
col_e = len(matrix[0])

col_no = len(matrix[0])-1
row_s = 1
row_e = len(matrix) - 1

# row_c = len(matrix)
# col_c = len(matrix[0])

print(f"matrix")
for r in range(len(matrix)):
    print(matrix[r])

for s in range(no_of_spirals):

    #top row

    print("top row")
    for j in range(col_s, col_e):
        print(matrix[row_no][j])
        print(f"[{row_no},{j}]")


    #right column
    print("right column")
    for i in range(row_s, row_e):
        print(matrix[i][col_no])
        print(f"[{i},{col_no}]")


    #bottom row
    print("bottom row")
    row_no_2 = len(matrix)-1-row_no
    if row_no_2 != row_no:
        for j in range(col_e - 1, col_s -1 , -1):
            print(matrix[row_no_2][j])
            print(f"[{row_no_2},{j}]")

    #left column
    print("left column")
    col_no_2 = len(matrix[0]) -1 - col_no
    if col_no_2 != col_no:
        for i in range(row_e-1, row_s -1 , -1):
            print(matrix[i][col_no_2])
            print(f"[{i},{col_no_2}]")

    row_no += 1
    col_s += 1
    col_e -= 1


    col_no -= 1
    row_s += 1
    row_e -= 1











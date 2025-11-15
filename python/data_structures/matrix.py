

print("1D Array")
arr = [0] * 100
print(arr)

print("2D Array")
arr = [[0] * 4]*5 # outer is the 1D
print(arr)

print(f''' length {len(arr)}''')

arr[0][0] = 1
print(arr)
print(f''' length of arr[0] {len(arr[0])}''')

print(f''' value at arr[0][0] {arr[0][0]}''')

print(f'''
        2D -> 1D
        index=i×col_count+j

        Going back (1D → 2D)
        row=index//col_count
        col=index%col_count''')

# 2D-> 1D index = i * col_count + j
# 1D -> 2D = row - index//col_count, col index%col_count


matrix = [[ i for i in range(4)] for j in range(7)]
print(f"matrix {matrix}")

matrix_mirror = [[matrix[i][j] for j in range(len(matrix[0])-1,-1,-1)] for i in range(0,len(matrix))]
print(f"matrix_mirror {matrix_mirror}")



for i, j in zip(range(1,10),range(1,10)):
    print(i)
    print(j)
    i = i+2

m = [[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12]]

for i in range(5,-1,-1):
    print(i)

rows_l = len(m)
cols_l = len(m[0])

for r in range(rows_l-1,-1,-1):
    for c in range(cols_l-1,-1,-1):
        print(f'''  {r},{c} : {m[r][c]} ''')


print('cols and rows')
flag = True
for c in range(cols_l-1,-1,-1):
    if flag:
        for r in range(rows_l-1,-1,-1):
            print(f'''  {r},{c} : {m[r][c]} ''')
        flag = False
    elif not flag:
        for r in range(0,rows_l,1):
            print(f'''  {r},{c} : {m[r][c]} ''')
        flag = True




'''
2 1 0
0 1 2 
2 1 0
'''

'''
-1 -2 -3
0 1 2
2 1 0

'''

chart = [
    [101, 102, 103, 104],
    [201, 202, 203, 204],
    [301, 302, 303, 304]
]

print(chart)

print(f"\nchart")
for r in range(len(chart)):
    print(chart[r])


# we do one row at a time -  value that changes is inside, value that doesn't change is outside


transpose_matrix = [[str(j) + ',' + str(i) for i in range(len(chart))] for j in range(len(chart[0]))]
print(f"\ntranspose_matrix")
for r in range(len(transpose_matrix)):
    print(transpose_matrix[r])
transpose_matrix = [[chart[i][j] for i in range(len(chart))] for j in range(len(chart[0]))]
print(f"\ntranspose_matrix")
for r in range(len(transpose_matrix)):
    print(transpose_matrix[r])

transpose_matrix = [[str(j) + ',' + str(i) for i in range(len(chart))] for j in range(len(chart[0])-1,-1,-1)]
print(f"\ntranspose_matrix")
for r in range(len(transpose_matrix)):
    print(transpose_matrix[r])

transpose_matrix = [[chart[i][j] for i in range(len(chart))] for j in range(len(chart[0])-1,-1,-1)]
print(f"\ntranspose_matrix")
for r in range(len(transpose_matrix)):
    print(transpose_matrix[r])

'''


[1,0,1,0,1]
[0,1,1,0,1]
[1,1,1,0,0]
[1,0,1,1,1]
[0,0,1,1,0]

{0: 1, 2: 12, 4: 2}
{0: 0, 
2: 2, 
7: 2, 
12: 2, 
17: 2, 
22: 2, 
23: 2, 
18: 2, 
19: 2, 
11: 2, 
6: 2, 
10: 2, 
15: 2, 
4: 4, 
9: 4}


'''
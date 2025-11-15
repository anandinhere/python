from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 20 10 00
        # 21 11 01
        # 22 12 02

        # 00 01 02
        # 10 11 12
        # 20 21 22

        # do one row at a time - index that changes will be inside, index that does change is outside
        e = [
            [matrix[j][i] for j in range(len(matrix) - 1, -1, -1)]
            for i in range(0, len(matrix))
        ]

        print(e)

        # 00 01 02 03 04
        # 10 11 12 13 14
        # 20 21 22 23 24
        # 30 31 32 33 34
        # 40 41 42 43 44

        # n - original size of matrix 5
        # n reduces by 2 for each iteration
        # c - count of circle starts from 0, increment once for every cirle
        # m - size of current matrix being dealt with 5
        # m starts from n
        # r no of rotations for each m ,  m -1
        # i0 j0 , i1 j1 , i2 j2 , i3 j3 are starting positions
        # i0 = m-1+c j0 = c
        # i1 = i0-r j1 = c
        # i2 = ii j2 = j1+r
        # i3 = i2 + c j3 = j2

        # 00 01 02 03 04
        # 10 11 12 13 14
        # 20 21 22 23 24
        # 30 31 32 33 34
        # 40 41 42 43 44

        # a -> b -> c ->  d -> a

        for l in matrix:
            print(l)
        print()

        n = len(matrix)
        c = 0  # diagonal number for j
        while n > 1:

            m = n
            r = m - 1 #no of rotations for each m
            print(f"m:{m} r:{r} c:{c} n:{n}")
            i0, j0 = m - 1 + c, c
            i1, j1 = i0 - r, c
            i2, j2 = i1, j1 + r
            i3, j3 = i0 , j2

            print(f" i0:j0 {i0}:{j0} , i1:j1 {i1}:{j1} , i2:j2 {i2}:{j2}, i3:j3 {i3}:{j3}  ")

            for r_ in range(r):
                temp = matrix[i0 - r_][j0]
                matrix[i0 - r_][j0] = matrix[i3][j3 - r_]
                matrix[i3][j3 - r_] = matrix[i2 + r_][j2]
                matrix[i2 + r_][j2] = matrix[i1][j1 + r_]
                matrix[i1][j1 + r_] = temp

                for l in matrix:
                    print(l)
                print()

            n -= 2
            c += 1

# m = [[1,2,3],
#      [4,5,6],
#      [7,8,9]]


m = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

#m = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]

'''
7 4 1
8 5 2
9 6 3

'''

Solution().rotate(m)
print(m)

'''
[[7, 4, 1], 
[4, 5, 2], 
[7, 8, 3]]

'''
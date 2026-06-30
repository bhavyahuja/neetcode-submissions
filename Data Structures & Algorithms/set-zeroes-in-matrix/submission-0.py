class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowset=set()
        colset=set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    rowset.add(i)
                    colset.add(j)

        print(rowset)
        print(colset)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rowset:
                    matrix[i][j]=0
                if j in colset:
                    matrix[i][j]=0
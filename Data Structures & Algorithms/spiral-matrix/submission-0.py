class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        steps=[len(matrix[0]),len(matrix)-1]
        dir=[(0,1),(1,0),(0,-1),(-1,0)]
        res=[]
        r,c,d=0,-1,0
        while steps[d&1]:
            for i in range(steps[d&1]):
                r+=dir[d][0]
                c+=dir[d][1]
                res.append(matrix[r][c])
            steps[d&1]-=1
            d+=1
            d%=4
        return res
            
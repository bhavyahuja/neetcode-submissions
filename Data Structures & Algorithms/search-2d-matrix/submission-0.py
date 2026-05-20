class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = []
        for row in matrix:
            for x in row:
                arr.append(x)
        l,r=0,len(arr)-1
        while(l<=r):
            m=(l+r)//2
            if(arr[m]>target):
                r=m-1
            elif(arr[m]<target):
                l=m+1
            else:
                return True
        return False
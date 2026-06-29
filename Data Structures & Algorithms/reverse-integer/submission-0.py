class Solution:
    def reverse(self, x: int) -> int:
        isn=0
        if x<0:
            isn=1
        x=abs(x)
        rev=int(str(x)[::-1])
        if rev>(1<<31)-1 or rev<-1*(1<<31):
            return 0
        if isn:
            return -1*rev
        return rev
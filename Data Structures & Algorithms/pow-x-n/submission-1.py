class Solution:
    def myPow(self, x: float, n: int) -> float:
        num=1
        if n>=0:
            for i in range(n):
                num*=x
        else:
            for i in range(abs(n)):
                num/=x
        return num
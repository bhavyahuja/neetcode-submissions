class Solution:
    def myPow(self, x: float, n: int) -> float:
        # num=1
        # if n>=0:
        #     for i in range(n):
        #         num*=x
        # else:
        #     for i in range(abs(n)):
        #         num/=x
        # return num

        res=1
        power=abs(n)
        while power:
            if power&1:
                res*=x
            x*=x
            power>>=1
        return res if n>=0 else 1/res
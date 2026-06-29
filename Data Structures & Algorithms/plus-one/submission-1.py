class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        num=0
        for i in range(n-1,-1,-1):
            num+=int(math.pow(10,n-i-1))*digits[i]
        num+=1
        ans=[]
        while num>0:
            ans.append(num%10)
            num//=10
        ans.reverse()
        return ans
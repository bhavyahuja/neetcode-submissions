class Solution:
    def isHappy(self, n: int) -> bool:
        visit=set()
        i=self.sumOfSquares(n)
        while i not in visit:
            if i==1:
                return True
            visit.add(i)
            i=self.sumOfSquares(i)
        return False

    def sumOfSquares(self, n: int) -> int:
        output = 0

        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10
        return output
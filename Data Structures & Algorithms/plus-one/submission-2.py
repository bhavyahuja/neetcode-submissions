class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # n=len(digits)
        # num=0
        # for i in range(n-1,-1,-1):
        #     num+=int(math.pow(10,n-i-1))*digits[i]
        # num+=1
        # ans=[]
        # while num>0:
        #     ans.append(num%10)
        #     num//=10
        # ans.reverse()
        # return ans

        one = 1
        i = 0
        digits.reverse()

        while one:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    one = 0
            else:
                digits.append(one)
                one = 0
            i += 1

        digits.reverse()
        return digits
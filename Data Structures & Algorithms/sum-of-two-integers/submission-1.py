class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        a &= MASK
        b &= MASK
        while b:
            new_sum = (a ^ b) & MASK
            new_carry = ((a&b) << 1) & MASK
            a = new_sum
            b = new_carry
        
        if (a<=MAX_INT): 
            return a 
        else: 
            return ~(a^MASK)

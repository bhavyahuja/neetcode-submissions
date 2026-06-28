class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a=b=c=False
        for x in triplets:
            if x[0]>target[0] or x[1]>target[1] or x[2]>target[2]:
                continue
            if x[0]==target[0]:
                a=True
            if x[1]==target[1]:
                b=True
            if x[2]==target[2]:
                c=True
        return a and b and c        
        
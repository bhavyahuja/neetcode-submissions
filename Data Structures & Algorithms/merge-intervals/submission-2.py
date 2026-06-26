class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans=[]
        intervals.sort()
        ans.append(intervals[0])
        for s,e in intervals[1:]:
            last=ans[-1]
            if last[1]>=s:
                last[1]=max(last[1],e)
            else:
                ans.append([s,e])
        return ans
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        # print(intervals)
        ans=0
        mains,maine=intervals[0][0], intervals[0][1]
        for s,e in intervals[1:]:
            if s<maine:
                ans+=1
                if e<maine:
                    maine=e
                    mains=s
                else:
                    continue
            maine=e
            mains=s
        return ans
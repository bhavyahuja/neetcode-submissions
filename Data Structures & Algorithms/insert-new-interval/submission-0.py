class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        appended=0
        ans=[]
        for s,e in intervals:
            if appended==1:
                ans.append([s,e])
                continue
            elif e<newInterval[0]:
                ans.append([s,e])
            elif appended==0 and s>newInterval[1]:
                ans.append(newInterval)
                ans.append([s,e])
                appended=1
            else:
                newInterval[0]=min(newInterval[0],s)
                newInterval[1]=max(newInterval[1],e)
        if not appended:
            ans.append(newInterval)
        return ans

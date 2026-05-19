class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        ans=[0]*len(temperatures)
        for i in range(len(temperatures)):
            if not stack:
                stack.append(i)
                continue
            if(temperatures[i]<=temperatures[stack[-1]]):
                stack.append(i)
            else:
                while stack and temperatures[i]>temperatures[stack[-1]]:
                    idx=stack.pop()
                    ans[idx]=i-idx
                stack.append(i)
        return ans
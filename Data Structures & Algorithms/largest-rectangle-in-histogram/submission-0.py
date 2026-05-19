class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        area=0
        stack=[]
        for i in range(len(heights)):
            if not stack:
                stack.append(i)
                continue
            while stack and heights[i]<heights[stack[-1]]:
                h = heights[stack.pop()]
                if stack:
                    w = i - stack[-1] - 1
                else:
                    w = i
                area=max(area, w*h)
            stack.append(i)

        while stack:
            h = heights[stack.pop()]
            if stack:
                w = len(heights) - stack[-1] - 1
            else:
                w = len(heights)
            area=max(area, w*h)
        return area
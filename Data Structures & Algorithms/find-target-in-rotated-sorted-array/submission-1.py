class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            m = (l+r)//2
            if nums[m] > nums[r]:
                l = m+1
            else:
                r = m
        if target>=nums[l] and target<=nums[len(nums)-1]:
            r=len(nums)-1
            while(l<=r):
                m=(l+r)//2
                if(nums[m]>target):
                    r=m-1
                elif(nums[m]<target):
                    l=m+1
                else:
                    return m
        else:
            r=l-1
            l=0
            while(l<=r):
                m=(l+r)//2
                if(nums[m]>target):
                    r=m-1
                elif(nums[m]<target):
                    l=m+1
                else:
                    return m
        return -1
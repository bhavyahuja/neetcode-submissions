class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt=Counter(tasks)
        # print(cnt)
        nums=[]
        for x in cnt:
            nums.append(cnt[x])
        nums.sort(reverse=True)
        print(nums)
        first=nums[0]
        i=0
        for w in range(len(nums)):
            if nums[w]==first:
                i+=1
            else:
                break
        print(i)
        ans=(first-1)*(n+1)+i
        return max(ans,len(tasks))
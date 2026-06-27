class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        arr=[]
        for i in range(len(gas)):
            arr.append(gas[i]-cost[i])
        print(arr)
        if sum(arr)<0:
            return -1
        tank=0
        start=0
        for i in range(len(arr)):
            if tank<0:
                tank=0
                start=i
            tank+=arr[i]
        return start
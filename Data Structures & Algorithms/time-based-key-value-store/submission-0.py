class TimeMap:

    def __init__(self):
        self.mp=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        l=0
        arr=self.mp[key]
        r=len(arr)-1
        ans=''
        while(l<=r):
            m=(l+r)//2
            if int(arr[m][0])<=timestamp:
                ans=arr[m][1]
                l=m+1
            else:
                r=m-1
        return ans

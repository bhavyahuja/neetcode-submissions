class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        cnt=Counter(hand)
        for x in sorted(cnt):
            if cnt[x]==0:
                continue
            freq=cnt[x]
            for y in range(x,x+groupSize):
                if cnt[y]<freq:
                    return False
                cnt[y]-=freq
        return True

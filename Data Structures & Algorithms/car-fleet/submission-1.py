class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=list(zip(position, speed))
        f=0
        cars.sort(reverse=True)
        # print(cars[speed])
        stack=[]
        for p,s in cars:
            finish=(target-p)/s
            if not stack or finish>stack[-1]:
                stack.append(finish)
                continue
            else:
                continue
        return len(stack)
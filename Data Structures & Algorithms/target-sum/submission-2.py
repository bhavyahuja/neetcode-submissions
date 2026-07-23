class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        if abs(target) > total:
            return 0

        if (total + target) % 2:
            return 0

        P = (total + target) // 2

        dp = [0] * (P + 1)
        dp[0] = 1

        for x in nums:
            for j in range(P, x - 1, -1):
                dp[j] += dp[j - x]

        return dp[P]
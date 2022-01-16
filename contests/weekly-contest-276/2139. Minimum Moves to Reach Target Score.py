class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans = 0
        while target > 1:
            if maxDoubles < 1:
                ans += target - 1
                break
            half = target // 2
            ans = ans + 1 + target % 2
            maxDoubles = maxDoubles - 1
            target = half
        return ans
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        l = 0
        r = sum(batteries)
        
        def check(x):
            return sum([min(x,b) for b in batteries]) >= n*x
        
        while l<=r:
            m = (l+r)//2
            if check(m):
                l = m+1
            else:
                r = m -1
        return r
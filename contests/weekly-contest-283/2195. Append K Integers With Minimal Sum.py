from typing import List


class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        def sum_r(l, r):
            s = ((l+r) * (r-l+1)) // 2
            return s
        
        
        ans = 0
        c = 0
        nums.sort()
        
        prev = 0
        
        for x in nums:
            
            if x == prev + 1 or x == prev:
                prev = x
                continue
            
            d = x - prev - 1
            
            if c + d >= k:
                ans += sum_r(prev+1, prev+k-c)
                c += d
                break
            else:
                ans += sum_r(prev+1, x-1)
                c += d
            prev = x
        
        if c < k:
            ans += sum_r(prev+1, prev+k-c)
        return ans
            
            
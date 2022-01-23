class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p = [x for x in nums if x>0] # all positive no
        n = [x for x in nums if x<0] # all negative no
        ans = []
        for a,b in zip(p,n):
            ans.append(a)
            ans.append(b)
        
        return ans
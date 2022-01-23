class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        m = defaultdict(int)
        for x in nums:
            m[x] += 1
        
        ans = []
        for k, v in m.items():
            if v == 1 and k-1 not in m and k+1 not in m:
                ans.append(k)
        
        return ans
            
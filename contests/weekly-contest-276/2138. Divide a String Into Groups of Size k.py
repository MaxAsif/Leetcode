class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = []
        for i in range(0,len(s), k):
            ans.append(s[i:i+k])
        
        f = len(ans[-1])
        for i in range(f, k):
            ans[len(ans)-1] += fill
        
        return ans
from typing import List

class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        ans = []
        
        
        r1,c1 = int(s[1]), s[0]
        r2,c2 = int(s[4]), s[3]
        
        for j in range(ord(c1), ord(c2)+1):
            for i in range(r1, r2+1):
                ans.append(f"{chr(j)}{i}")
        
        return ans
                        
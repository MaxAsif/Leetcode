from typing import List

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        def gcd(a, b):
            if b == 0:
                return a
            
            return gcd(b, a%b)
        
        def lcm(a, b):
            return (a*b)//gcd(a,b)
        
       
        st = []
        for n in nums:
            st.append(n)
            while len(st) > 1 and gcd(st[-1], st[-2]) > 1:
                x = st.pop()
                y = st.pop()
                st.append(lcm(x,y))
        
        return st
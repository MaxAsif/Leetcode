class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        dp = {}
        
        def dfs(i):
            if i >= len(questions):
                return 0
            
            if i in dp:
                return dp[i]
            
            dp[i] = max( dfs(i+questions[i][1]+1) + questions[i][0], dfs(i+1) )
            
            return dp[i]
        
        dfs(0)
        #print(dp)
        return dp[0]
        
        
        
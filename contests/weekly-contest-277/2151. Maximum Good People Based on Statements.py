class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        n = len(statements)
        # total possibilties
        total_comb = 2 ** n
        ans = 0
        

        # calculate total  set bit (i.e, no of good people)
        def set_bit(x):
            c = 0
            while x > 0:
                if x & 1:
                    c += 1
                x = x >> 1
            return c
        
        # find jth bit value
        def jth_bit(x,j):
            return x & (1<<j) > 0
        
        # check if the current combination is valid or not
        def is_valid(x):
            for i in range(n):
                for j in range(n):
                    if statements[i][j] == 2:
                        continue
                    ii = jth_bit(x, i) # i'th is good or bad
                    jj = jth_bit(x, j) # j'th is good or bad
                    
                    # only condradict when ii is a good person and statement made by him about j 
                    # does not match with current combination
                    if jj != statements[i][j] and ii: 
                        return False
            return True
                        
        # iterate all possible combination       
        for i in range(total_comb-1, -1, -1):
            if is_valid(i):
                curr = set_bit(i)
                ans = max(ans, curr)
        
        return ans
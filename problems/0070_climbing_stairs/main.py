# recursive solution: does not accept on LeetCode (not optimal)
class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(i):
            # base case
            if i >= n:
                return i == n
            # recursive Case
            return dfs(i+1) + dfs (i+2)
        return dfs(0)

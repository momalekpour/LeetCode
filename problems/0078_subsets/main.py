class Solution:
    # Time Complexity: (number of subsets)×(time to copy each) = 2^n × O(n) = O(n . 2^n)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # store all subsets
        res = []
        # store current subset we are building up
        subset = []

        def dfs(i):
            # base case: if we've considered all elements
            if i >= len(nums):
                res.append(subset.copy())
                return

            # choice 1: include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # backtrack
            subset.pop()

            # choice 1: exclude nums[i]
            dfs(i + 1)

        dfs(0)
        return res

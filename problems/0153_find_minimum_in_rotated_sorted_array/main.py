class Solution:
    def findMin(self, nums: List[int]) -> int:
        ## Solution 1: brute force - time O(n), space O(1)
        # traverse the array and find the minimum value
        # return min(nums)

        ## Solution 2: time O(log n)
        # finding a lower bound
        # e.g: [3, 4, 5, 1, 2]
        # e.g: [6, 7, 1, 2, 3, 4, 5]
        # e.g: [1, 2, 3, 4, 5]

        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ## Solution 1: brute force - time O(n), space O(1)
        # linear search of array
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        # return -1

        ## Solution 2: time O(log n), space O(1)
        # e.g: [4, 5, 6, 7, 0, 1, 2] & t = 0
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        pivot = l

        def binary_search(nums, left, right, target):
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
            return -1

        if target >= nums[0] and pivot != 0:
            left, right = 0, pivot - 1
        else:
            left, right = pivot, len(nums) - 1

        return binary_search(nums, left, right, target)

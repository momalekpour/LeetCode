# Iterative binary search - Time: O(log n) Space: O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1

        while L <= R:
            M = (L + R) // 2
            if target < nums[M]:
                R = M - 1
            elif target > nums[M]:
                L = M + 1
            else:
                return M

        return -1


# Recursive binary search - Time: O(log n) Space: O(log n)
class Solution:
    def binary_search(self, l, r, nums, target):
        if l > r:
            return -1
        m = (l + r) // 2

        if target == nums[m]:
            return m
        elif target < nums[m]:
            return self.binary_search(l, m - 1, nums, target)
        else:
            return self.binary_search(m + 1, r, nums, target)

    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(l=0, r=len(nums)-1, nums=nums, target=target)

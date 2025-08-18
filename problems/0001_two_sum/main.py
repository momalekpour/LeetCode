class Solution:
    # Hashmap Solution: time and space complexity -> O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {} # val -> idx
        for i, num in enumerate(nums):
            diff = target - num
            if diff in prev_map:
                return [prev_map[diff], i]
            prev_map[num] = i

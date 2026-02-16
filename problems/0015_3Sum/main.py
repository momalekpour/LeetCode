class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ## Solution 1: brute force time O(n^3) - space O(m) m is number of rtiplet
        # triplets = set()
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         for k in range(j+1, n):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 triplets.add(tuple(sorted((nums[i], nums[j], nums[k]))))
        # return [list(t) for t in triplets]

        ## Solution 2: time O(n^3)
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res

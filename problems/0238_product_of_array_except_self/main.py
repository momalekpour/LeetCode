class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ## Solution 1: time O(n) - Space O(n)
        # prefix = [None] * len(nums)
        # postfix = [None] * len(nums)
        # res = []

        # for i in range(len(nums)):
        #     mult = prefix[i - 1] * nums[i] if i > 0 else nums[i]
        #     prefix[i] = mult
        # for i in range(len(nums)-1, -1, -1):
        #     mult = postfix[i + 1] * nums[i] if i < len(nums)-1 else nums[i]
        #     postfix[i] = mult
        # for i in range(len(nums)):
        #     pre_m = prefix[i-1] if i > 0 else 1
        #     post_m = postfix[i+1] if i < len(nums)-1 else 1
        #     res.append(pre_m * post_m)

        # return res

        ## Solution 2: time O(n) - space O(1)
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res

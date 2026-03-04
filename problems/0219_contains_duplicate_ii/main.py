class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ## Solution 1: brute force - time O(n^2), space O()
        ## e.g: [1,2,3,1,2,3]
        ##       l     r
        # for l in range(len(nums)):
        #     for r in range(l + 1, min(l + k + 1, len(nums))):
        #         if nums[l] == nums[r]:
        #             return True
        # return False

        ## Solution 2: one pass iteration / sliding window
        ## complexity: time O(n), space O(min(n,k))
        ##       l
        ## e.g: [1,2,3,1,2,3]
        ##           r

        window = set()
        l = 0
        for r in range(len(nums)):
            if nums[r] in window:
                return True
            window.add(nums[r])
            if r - l + 1 > k:
                window.remove(nums[l])
                l += 1
        return False

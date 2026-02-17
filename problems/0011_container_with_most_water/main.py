class Solution:
    def maxArea(self, height: List[int]) -> int:
        ## Solution 1: brute force - time O(n^2)
        # areas = []
        # for i in range(len(height)):
        #     for j in range(i + 1, len(height)):
        #         x = j - i
        #         y = min(height[i], height[j])
        #         a = x * y
        #         areas.append(a)
        # return max(areas)

        ## Solution 2: two pointers - time O(n) space O(1)
        a = 0
        l, r = 0, len(height) - 1
        while l < r:
            new_a = (r - l) * min(height[l], height[r])
            a = max(a, new_a)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return a

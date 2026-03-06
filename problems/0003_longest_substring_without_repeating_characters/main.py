class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ## Solution 1: brute force - time O(n^2), space O(n)

        ## Solution 2: one pass sliding window - time O(n), space O(n)
        #      l
        # e.g: abcabcbb
        #         r

        l = 0
        max_length = 0
        sub_s = set()
        for r in range(len(s)):
            # shrink the window from the left until the duplicate is removed.
            while s[r] in sub_s:
                sub_s.remove(s[l])
                l += 1
            sub_s.add(s[r])
            max_length = max(max_length, len(sub_s))
        return max_length

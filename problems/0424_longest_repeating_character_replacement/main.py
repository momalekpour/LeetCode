class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ## Solution 1: brute force - time O(n^2), space O(m)
        ##           i
        ## e.g: s = "ABAB", k = 2
        ##            j
        # res = 0
        # for i in range(len(s)):
        #     chars = {}
        #     tmp = 0
        #     for j in range(i, len(s)):
        #         chars[s[j]] = chars.get(s[j], 0) + 1
        #         max_freq = max(chars.values())
        #         current_len = j - i + 1
        #         if current_len - max_freq <= k:
        #             res = max(res, current_len)
        #         else:
        #             break
        # return res

        ## Solution 2: sliding window - time O(m*n), space O(m)
        ##           l
        ## e.g: s = "ABAB", k = 2
        ##            r
        l = 0
        chars = {}
        res = 0
        for r in range(len(s)):
            chars[s[r]] = chars.get(s[r], 0) + 1
            max_freq = max(chars.values())
            curr_len = r - l + 1
            if curr_len - max_freq <= k:
                res = max(res, curr_len)
            else:
                chars[s[l]] -= 1
                l += 1
        return res

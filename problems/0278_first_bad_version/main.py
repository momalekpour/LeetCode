# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# Iterative binary search: time: O(log n), space: O(1)
class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        first_bad_version = -1

        while l <= r:
            version = (l + r) // 2
            if isBadVersion(version):
                first_bad_version = version
                r = version - 1
            else:
                l = version + 1

        return first_bad_version

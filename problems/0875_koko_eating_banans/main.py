# Brute Force: time O(m * n), space O(1), where n is the length of the input array piles and m is the maximum number of bananas in a pile
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # how much time does it take koko it pile with x bananas? ceil(x / k)
        # k lower bound: 1
        # k upper bound: max pile
        minimum_k = max(piles)
        for k in range(1, max(piles) + 1):
            if self.is_possible(piles, k, h):
                minimum_k = k
                break
        return minimum_k

    def is_possible(self, piles, k, h):
        total_time = 0
        for pile in piles:
            total_time += math.ceil(pile / k)
        return True if total_time <= h else False


# Binary Search: time O(n*log(m)), space O(1), where n is the length of the input array piles and m is the maximum number of bananas in a pile
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # how much time does it take koko it pile with x bananas? ceil(x / k)
        # k lower bound: 1
        # k upper bound: max pile
        l, r = 1, max(piles)
        minimum_k = max(piles)

        while l <= r:
            k = (l + r) // 2
            if self._is_possible(piles, k, h):
                minimum_k = k
                r = k - 1
            else:
                l = k + 1

        return minimum_k

    def _is_possible(self, piles, k, h):
        total_time = 0
        for pile in piles:
            total_time += math.ceil(pile / k)
        return True if total_time <= h else False

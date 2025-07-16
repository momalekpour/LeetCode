# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

# time: O(log n), space: O(1)
class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n

        while low <= high:
            num = (low + high) // 2
            status = guess(num)
            if status == -1:
                high = num - 1
            elif status == 1:
                low = num + 1
            elif status == 0:
                return num

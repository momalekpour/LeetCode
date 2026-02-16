class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ## Solution 1: O(n.log(n))
        # count_map = {}
        # for n in nums:
        #     count_map[n] = count_map.get(n, 0) + 1
        # sorted_list = sorted(count_map.items(), key=lambda item: item[1], reverse=True)
        # return [n for n,c in sorted_list][:k]

        ## Solution 2: O(n)
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        freq = [[] for i in range(len(nums)+1)]
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for idx in range(len(freq) - 1, 0, -1):
            for n in freq[idx]:
                res.append(n)
                if len(res) == k:
                    return res

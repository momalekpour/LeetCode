class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ## Solution 1: log(m.nlogn)
        # words_map = {}
        # for word in strs:
        #     sorted_word = sorted(word)
        #     sorted_word = "".join(sorted_word)
        #     if sorted_word in words_map:
        #         words_map[sorted_word].append(word)
        #     else:
        #         words_map[sorted_word] = [word]

        # res = []
        # for k, v in words_map.items():
        #     res.append(v)
        # return res

        ## Solution 2: O(m.n)
        words_map = dict()
        for s in strs:
            chars_count = [0] * 26
            for c in s:
                chars_count[ord(c) - ord("a")] += 1
            chars_count = tuple(chars_count)
            if chars_count in words_map:
                words_map[chars_count].append(s)
            else:
                words_map[chars_count] = [s]
        return list(words_map.values())

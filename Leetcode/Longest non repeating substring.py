class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_s = ""
        count = 0
        for val in s:
            if val not in sub_s:
                sub_s += val

            else:
                sub_s = sub_s[sub_s.index(val) + 1:]
                sub_s += val

            if len(sub_s) > count:
                count = len(sub_s)

        return count
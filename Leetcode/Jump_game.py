class Solution:
    def canJump(self, s: List[int]) -> bool:
        temp = 0
        if len(s) == 1:
            return True
        for i in reversed(range(len(s))):
            if s[i] + i >= temp:
                temp = i
                continue
        if temp == 0:
            return True
        return False
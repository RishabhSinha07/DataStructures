class Solution:
    def middle_out(self, s, left_most, right_most, i, z):
        left = i
        right = z
        x_, y_ = 0, 0
        while left >= left_most and right <= right_most:
            if s[left] == s[right]:
                x_ = left
                y_ = right
                left -= 1
                right += 1
            else:
                break
        return (y_ - x_ + 1), x_, y_

    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 0:
            return ""
        left_most = 0
        right_most = len(s) - 1
        range_ = 0
        x, y = 0, 0
        for z in range(len(s)):
            temp, x_, y_ = self.middle_out(s, left_most, right_most, z, z)
            temp1, x1_, y1_ = self.middle_out(s, left_most, right_most, z, z + 1)
            if temp1 > temp:
                temp = temp1
                x_ = x1_
                y_ = y1_
            if temp > range_:
                range_ = temp
                x = x_
                y = y_
                print("x,y", x, y)
        return s[x:y + 1]
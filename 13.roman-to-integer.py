#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        roman={ 'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        x=roman[s[0]]
        r=0
        for i in range(1, len(s)):
            if roman[s[i-1]]<roman[s[i]]:
                r=roman[s[i]]-roman[s[i-1]]
                x=x+r-roman[s[i-1]]

            else:
                x+=roman[s[i]]

        return x
# @lc code=end


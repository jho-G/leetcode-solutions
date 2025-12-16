#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#

# @lc code=start
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))              
        nums.sort(reverse=True)              
        if len(nums) >= 3:
            return nums[2]                  
        else:
            return nums[0]


        # @lc code=end


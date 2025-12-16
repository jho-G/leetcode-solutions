#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self,ns,target):
        nums={}
        for x,y in enumerate(ns):
            solution=target-y
            if solution in nums:
                return [nums[solution],x] 
            nums[y]=x
        
# @lc code=end


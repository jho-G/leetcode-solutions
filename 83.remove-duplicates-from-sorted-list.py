#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        values=set()
        current=head
        values.add(current.val)
        while current.next:
            if current.next.val in values:
                current.next=current.next.next
            else:
                values.add(current.next.val)
                current=current.next
        return head
        
# @lc code=end


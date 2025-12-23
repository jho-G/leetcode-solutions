#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None
        less_dummy=ListNode(0)
        more_dummy=ListNode(0)

        less=less_dummy
        more=more_dummy
        current=head

        while current:
            if current.val < x:
                less.next=current
                less=less.next
            else:
                more.next=current
                more=more.next
            current=current.next

        more.next=None
        less.next=more_dummy.next

        return less_dummy.next
# @lc code=end


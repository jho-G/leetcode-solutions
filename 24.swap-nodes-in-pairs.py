#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev=dummy
        first=head

        while first and first.next:
            second=first.next

            prev.next=second
            first.next=second.next
            second.next=first

            prev=first
            first=first.next

        self.head=dummy.next
        return self.head
# @lc code=end


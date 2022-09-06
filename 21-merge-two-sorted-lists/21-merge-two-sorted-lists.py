# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x = ListNode()
        y = x
        while l1 and l2:
            if l1.val < l2.val:
                y.next = l1
                l1 = l1.next
            else:
                y.next = l2
                l2 = l2.next
            y = y.next
        if l1:
            y.next = l1
        else:
            y.next = l2
        return x.next
        
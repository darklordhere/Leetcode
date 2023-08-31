# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        class p:
            def __init__(self, x):
                self.val = x
                self.next = None
        a,b = [],[]
        while l1:
            a.append(str(l1.val))
            l1 = l1.next
        while l2:
            b.append(str(l2.val))
            l2 = l2.next
        x = [int(i) for i in list(str(int(("".join(a))[::-1])+int(("".join(b))[::-1]))[::-1])]
        def list_to_lst(x):
            c = d = p(0)
            for i in x:
                c.next = p(i)
                c = c.next
            return d.next
        
        return list_to_lst(x)
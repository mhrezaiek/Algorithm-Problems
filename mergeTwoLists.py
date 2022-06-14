# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        mainlist=dummy
        while list1 or list2:
            a=1000
            b=1000
            if list1 is not None:
                a=list1.val
            if list2 is not None:
                b=list2.val
            if a<=b:
                mainlist.next=ListNode(a)
                mainlist=mainlist.next
                if list1 is not None:
                    list1=list1.next
                
            else:
                mainlist.next=ListNode(b)
                mainlist=mainlist.next
                if list2 is not None:
                    list2=list2.next
                
        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head 
        if not curr:
            return curr 
        nxt = curr.next
        
        while curr.next:
            nxt = curr.next
            if curr.val == nxt.val:
                curr.next = nxt.next
            else:
                curr = curr.next
        return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curra = headA 
        nums =set()
        while curra :
            nums.add(curra)
            curra = curra.next
        curr = headB
        while curr:
            if curr in nums:
                return curr
            curr = curr.next
        
            

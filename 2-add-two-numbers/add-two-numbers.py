# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        while l1 is not None or l2 is not None or carry != 0:
            # Get values from current nodes, or 0 if a list has ended
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            
            # Compute sum and new carry
            total = val1 + val2 + carry
            carry = total // 10
            new_digit = total % 10
            
            # Create a new node with the digit and attach it
            current.next = ListNode(new_digit)
            current = current.next
            
            # Advance pointers
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
                
        return dummy_head.next
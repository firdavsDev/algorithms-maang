# Add 2 Nodes
class ListNode: 
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(0)
        L3: ListNode = dummy_head

        carry = 0

        while (l1 or l2):
            l1_val = l1 is not None ? l1.val : 0
            l2_val = l2 is not None ? l2.val : 0

            current_sum = l1_val + l2_val + carry
            carry = current_sum/10
            last_digit = current_sum % 10

            new_node = ListNode(last_digit)
            L3.next = new_node

            if (l1 is not None):
                
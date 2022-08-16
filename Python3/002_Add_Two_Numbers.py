# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        result = ListNode()
        current_node = result

        while l1 or l2 or carry:
            val_1 = l1.val if l1 else 0
            val_2 = l2.val if l2 else 0

            val = val_1 + val_2 + carry
            carry = val // 10
            val = val % 10

            current_node.next = ListNode(val)
            current_node = current_node.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return result.next

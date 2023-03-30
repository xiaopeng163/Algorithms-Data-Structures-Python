# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

        new_head = head
        if head.next:
            new_head = self.reverseList(head=head.next)
            head.next.next = head

        head.next = None
        return new_head


s = Solution()
head = ListNode(
    val=1,
    next=ListNode(
        val=2, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5)))
    ),
)
s.reverseList(head=head)

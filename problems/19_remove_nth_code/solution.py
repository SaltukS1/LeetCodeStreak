# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        first = second = dummy

        # first göstericiyi n + 1 adım ileri gönderiyoruz
        for _ in range(n + 1):
            first = first.next

        # first sona ulaşana kadar ilerliyoruz
        while first:
            first = first.next
            second = second.next

        # second'ın bir sonraki düğümünü atlayarak siliyoruz
        second.next = second.next.next

        return dummy.next

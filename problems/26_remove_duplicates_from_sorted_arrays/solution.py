class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        prev_group = dummy

        while True:
            # Grubun son node'unu bul
            kth = self.get_kth_node(prev_group, k)
            if not kth:
                break  # yeterli node yoksa işlemi bitir

            group_next = kth.next

            # Reverse işlemi
            prev, curr = kth.next, prev_group.next
            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # bağlantıları güncelle
            temp = prev_group.next
            prev_group.next = kth
            prev_group = temp

        return dummy.next

    def get_kth_node(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

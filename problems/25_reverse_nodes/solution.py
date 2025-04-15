class Solution:
    def reverseKGroup(self, head, k):
        # Kadar node kaldı mı kontrolü
        count = 0
        node = head
        while node and count < k:
            node = node.next
            count += 1
        
        if count < k:
            return head  # Ters çevirmiyoruz

        # Reverse k nodes
        prev, curr = None, head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # head şu an grubun son node'u oldu, onun next'ini geri kalan grubun çözümüne bağla
        head.next = self.reverseKGroup(curr, k)
        return prev

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        while l1 or l2 or carry:
    
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            
      
            total = x + y + carry
            carry = total // 10
            
    
            current.next = ListNode(total % 10)
            current = current.next
            
           
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy_head.next

# Test code
def create_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def print_linked_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values

# Test with example 1
if __name__ == "__main__":
   
    l1 = create_linked_list([2,4,3])
    l2 = create_linked_list([5,6,4])
    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)
    print(print_linked_list(result)) 
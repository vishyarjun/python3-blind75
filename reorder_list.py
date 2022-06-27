class Solution:
    def reorderList(self, head: ListNode) -> None:
        stk = []
        output = ListNode(-1)
        output.next = head
        node = head
        while node:
            stk.append(node)
            node = node.next
        
        while True:
            if head==stk[-1]:
                head.next=None
                break
            bottom = stk.pop()
            bottom.next = None
            temp = head.next
            head.next = bottom
            if bottom==temp:
                break
            bottom.next = temp
            head = bottom.next
        
        return output.next

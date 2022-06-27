class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ctrf = 0
        bk_node = None
        out = ListNode(-1)
        out.next = head
        node = out
        while node:
            ctrf+=1
            if bk_node:
                bk_node = bk_node.next
            if ctrf==n+1:
                bk_node = out
            node = node.next
        if bk_node and bk_node.next:
            bk_node.next = bk_node.next.next
            return out.next

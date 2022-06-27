class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return
        if len(lists)==1:
            return lists[0]
        
        hp =[]
        
        for lst in lists:
            while lst:
                heapq.heappush(hp,lst.val)
                lst=lst.next
        output = ListNode(0)
        node = output
        while hp:
            node.next = ListNode(heapq.heappop(hp))
            node=node.next
        
        
        return output.next
                        

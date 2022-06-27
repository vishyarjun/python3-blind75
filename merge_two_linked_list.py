# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        output = ListNode(-1)
        node = output
        while head1 and head2:
            if head1.val <= head2.val:
                node.next = ListNode(head1.val)
                head1=head1.next
            else:
                node.next = ListNode(head2.val)
                head2=head2.next
            node = node.next
        while head1:
            node.next = ListNode(head1.val)
            head1=head1.next
            node = node.next
        while head2:
            node.next = ListNode(head2.val)
            head2=head2.next
            node = node.next
        return output.next

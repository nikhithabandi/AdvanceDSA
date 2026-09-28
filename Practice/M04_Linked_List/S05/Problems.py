
# 876.middle of the linked list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow


#876.Middle of the Linked List
#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        count=0
        temp=head
        while temp :
            count+=1
            temp = temp.next 
        middle_ind = count//2
        temp=head
        for i in range(middle_ind):
            temp=temp.next
        return temp
    
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
solution = Solution()
middle = solution.middleNode(head)
print(middle.val)


# 141. Linked List Cycle
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False


# 21. Merge Two Sorted Lists
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        temp=ListNode()
        curr=temp
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        if list1:
            curr.next=list1
        else:
            curr.next=list2
        return temp.next



# 206. Reverse Linked List
class Solution:

  def reverseList(self, head: ListNode | None) -> ListNode | None:
    prev = None
    curr = head

    while curr:
      next_node = curr.next  # 1. Save the next node
      curr.next = prev  # 2. Reverse the link
      prev = curr  # 3. Move 'prev' forward
      curr = next_node  # 4. Move 'curr' forward

    return prev  # 'prev' is now the new head of the reversed list
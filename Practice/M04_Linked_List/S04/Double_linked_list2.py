class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    if head is not None:
        head.prev = new_node
    return new_node

#insert a node at the end
def insert_at_end(head, data):
    new_node = Node(data)
    if head is None:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    new_node.prev = current
    return head

def count_nodes(self):
    if self.head is None:
        return 0
    if self.head.next is None:
        return 1
    temp = self.head
    count=0
    while temp:
        count+=1
        temp=temp.next
    return count


def delete_begin(self):
    if self.head is None:
        return 
    self.head=self.head.next
def count_nodes(self):
    if self.head is None:
        return 0
    if self.head.next is None:
        return 1 
    
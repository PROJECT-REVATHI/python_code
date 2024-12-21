class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the linked list with no nodes (head is None)

# Create a linked list object
linked_list = LinkedList()

# Create a new node
new_node = Node(4)

# Insert the new node at the beginning of the linked list
new_node.next = linked_list.head  # Point new_node's next to the current head
linked_list.head = new_node       # Update head to the new_node

# Verify the head node
print("Head Node Data:", linked_list.head.data)  # Should print: Head Node Data: 4

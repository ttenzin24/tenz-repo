class Node:
    def __init__(self, data):
        # Initialize the data attribute of the node with the given data.
        self.data = data
        # Initialize the next attribute of the node as None,
        # indicating that it initially does not point to any other node as it's empty.
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        # Initialize the head attribute of the linked list as None, indicating an empty list.
        self.head = None

    def append(self, data):
        # Create a new node object with the given data.
        new_node = Node(data)
        # Check if the linked list is empty.
        if not self.head:
            # If the linked list is empty, set the new node as the head of the linked list and return.
            self.head = new_node
            return
        # If the linked list is not empty, traverse the linked list to find the last node.
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        # Once the last node is found, set the next attribute of the last node to the new node,
        # effectively adding it to the end of the linked list.
        last_node.next = new_node

    def display(self):
        # Start from the head of the linked list.
        current = self.head
        # Traverse the linked list and print the data of each node.
        while current:
            print(current.data, end=" -> ")
            # Move to the next node in the linked list.
            current = current.next
        # Print "None" to signify the end of the linked list.
        print("None")

# Example usage:
# Create an instance of the SinglyLinkedList class.
s = SinglyLinkedList()
# Append some elements to the linked list.
s.append(13)
s.append(24)
s.append(36)
s.append(90)
# Display the elements of the linked list.
s.display()

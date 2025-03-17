class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node

class LinkedList:
    def __init__(self):
        self.head = None  # Initially, the list is empty

    def append(self, data):
        """Add a node at the end of the list"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def prepend(self, data):
        """Add a node at the beginning of the list"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        """Delete the first occurrence of a node with the given value"""
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next  # Move head to the next node
            temp = None
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if not temp:
            return  # Key not found

        prev.next = temp.next
        temp = None  # Remove node

    def display(self):
        """Print all nodes in the list"""
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Example usage
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.prepend(5)
ll.display()  # Output: 5 -> 10 -> 20 -> 30 -> None

ll.delete(20)
ll.display()  # Output: 5 -> 10 -> 30 -> None

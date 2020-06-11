"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        new_node = ListNode(value, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length = self.length + 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        # # if there is no head then return none
        value = self.head.value
        self.delete(self.head)
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        # if there is no tail return null
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            old_node_prev = self.tail
            self.tail = new_node
            old_node_prev.next = self.tail
            self.tail.prev = old_node_prev
            self.length += 1

        # else access the next until we get to the very end

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):

        # if no tail then return none
        if self.tail is None:
            return None
            # if head and tail are the same return reset values for head tail and length
        elif self.head == self.tail:
            test = self.tail.value
            self.head = None
            self.tail = None
            self.length = 0
            return test
            # else while loop through until the node.prev.next is none and capture it, set tail to captured object, set tail.next to none, return captured object.value
        else:
            value = self.tail.value
            self.delete(self.tail)
            return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        # check if there is a head and a tail, if not return None
        if self.head and self.tail is None:
            return None
        elif self.head == self.tail:
            return None
        elif node == self.head:
            return None
        elif node == self.tail:
            self.tail = node.prev
            node.next = self.head.prev
            node.prev = None
            node = self.head

        # check if head and tail are pointing to the same node, if yes, then do nothing because its alreading head and tail

        # if node equals head then do nothing because its already first thing in the list

        # if node equals tail then get the previous node and set that to the tail

        # else delete current node location and use the value in the node to add to head.

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        pass
        # check if there is a head and a tail, if not return None

        # check if head and tail are pointing to the same node, if yes, then do nothing because its alreading head and tail

        # if node equals tail then do nothing because its already the last thing in the list

        # if node equals head then get the next node and set that to the head

        # else delete current node location and use the value in the node to add to tail.

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        # if no head or tail return none
        if self.head and self.tail is None:
            return None

        self.length -= 1
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.head == node:
            print(node.value)
            print(node.next.value)
            self.head = node.next
            node.delete()
        elif self.tail == node:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()

    """Returns the highest value currently in the list"""

    def get_max(self):
        pass
        # current_node = self.head
        # while current_node.next is not None:
        # current_node = self.head.next

        # check the value of the old head and compare it the the current one return the highest value

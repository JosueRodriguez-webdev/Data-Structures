"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):

        # make a new node input for the value being passed in as argument
        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

        # check if the new value is greater, less, or equal to the root value
        # if it is lower check to see if the root has space, if not check child / sub tree - repeat for right side

        # Return True if the tree contains the value
        # False if it does not

    def contains(self, target):
        if target == self.value:
            return True
        if target < self.value:
            if self.left is None:
                return False
            else:
                self.left.contains(target)
        if target > self.value:
            if self.right is None:
                return False
            else:
                self.left.contains(target)

        # check if target is greater than root, then:
        # if target == self.value, then return true
        # else recursion self.right.contain(target)

        # check if target is less than root, then:
        # if target == self.value, then return true
        # else recursion self.left.contain(target)

        # check if self.value == none, then return false

        # Return the maximum value found in the tree

    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `fn` on the value of each node

    def for_each(self, fn):
        pass
        # Part 2 -----------------------

        # Print all the values in order from low to high
        # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

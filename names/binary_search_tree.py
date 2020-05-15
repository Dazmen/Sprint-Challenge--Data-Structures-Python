
class BinarySearchTree:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value is None:
            self.value = value
        elif value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        elif value >= self.value:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        if target == self.value:
            return True
        if target < self.value:
            if self.left is None:
                return None
            else:
                return self.left.contains(target)
        if target > self.value:
            if self.right is None:
                return None
            else:
                return self.right.contains(target)


   
    

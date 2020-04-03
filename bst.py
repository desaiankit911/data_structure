"""
it contain 2 classes

1. node class
2. binary search tree class
"""
#node class

class node:
    def __init__(self,value=None):
        self.value = value
        self.left_child = None    #left of node (smaller tha node)
        self.right_child = None   #right of node (bigger than node)

#binary search tree class
class bst:
    def __init__(self):
        self.root = None

    #insert method
    def insert(self,value):
        #if no node than start with node || insert value
        if self.root == None:
            self.root = node(value)
        else:
            self._insert(value,self.root)
        
    def _insert(self,value,cur_node):
        if value < cur_node.value:
            if cur_node.left_child == None:
                cur_node.left_child = node(value)
            else:
                self._insert(value,cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child = node(value)
            else:
                self._insert(value,cur_node.right_child)
        else:
            print("value already exist")
        
    def print_bst(self):
        if self.root != None:
            self._print_bst(self.root)
    
    def _print_bst(self,cur_node):
        if cur_node != None:
            self._print_bst(cur_node.left_child)
            print(cur_node.value)
            self._print_bst(cur_node.right_child)

    def bst_height(self):
        if self.root != None:
            return self._bst_height(self.root,0)
        else:
            return 0

    def _bst_height(self,cur_node,cur_height):
        if cur_node == None:
            return cur_height
        left_height = self._bst_height(cur_node.left_child,cur_height +1)
        right_height = self._bst_height(cur_node.right_child,cur_height +1)
        return max(left_height,right_height)

    def search(self,value):
        if self.root != None:
            return self._search(value,self.root)
        else:
            return False
    
    def _search(self,value,cur_node):
        if value == cur_node.value:
            return True
        elif value < cur_node.value and cur_node.left_child != None:
            return self._search(value,cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child != None:
            return self._search(value,cur_node.right_child)
        else:
            return False

tree = bst()

tree.insert(13)
tree.insert(11)
tree.insert(2)
tree.insert(5)
tree.insert(8)
tree.insert(3)
tree.insert(23)
tree.insert(21)
tree.insert(10)
tree.insert(22)

tree.print_bst()
print("bst height : {}".format(tree.bst_height()))



print(tree.search(8))
print(tree.search(10))
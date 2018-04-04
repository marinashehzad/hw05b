import random

########## Nodes.
# Nodes to be used in trees.

class TreeNode:
    '''A node in a binary tree.'''
    def __init__(self, n):
        self.data = n
        self.left = self.right = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return self.__str__()

    def num_children(self):
        '''N.num_children() -> int

        Returns the number of children of N that are not None.
        '''
        return sum([1 for child in [self.left, self.right] if child])

class TreapNode(TreeNode):
    '''A node in a treap.'''
    def __init__(self, data, priority):
        super().__init__(data)  # Parent constructor.
        self.priority = priority

    def __str__(self):
        return "({}, {})".format(self.data, self.priority)
        
class AvlNode(TreeNode):
    '''A node in an AVL tree.'''
    def __init__(self, data):
        super().__init__(data)  # Parent constructor.
        self.height = 0

    def __str__(self):
        return "({}, {})".format(self.data, self.height)

########## Trees. ##########
# Trees utilizing above nodes. Use helper functions defined outside
# the class to achieve functionality.

class Bst:
    '''A BST. Does not contain duplicates. Nodes are of type TreeNode.'''
    def __init__(self):
        self.root = None
        self.size = 0

    def __str__(self):
        return tree_string(self.root)
    
    def __repr__(self):
        return self.__str__()
        
    def add(self, n):
        self.root, added = bst_add(self.root, n)
        if added:
            self.size += 1
        return added
    
    def find(self, n):
        return bst_find(self.root, n)
    
    def remove(self, n):
        self.root, removed = bst_remove(self.root, n)
        if removed:
            self.size -= 1
        return removed

    def clear(self):
        self.__init__()
        
class Treap(Bst):
    '''A treap. Does not contain duplicates. Nodes are of type TreapNode.'''
    max_priority = 1 << 10
    def __init__(self):
        super().__init__()
        self.priorities = set()
        
    def add(self, n):
        priority = random.randint(0, Treap.max_priority)
        while priority in self.priorities:
            priority = random.randint(0, Treap.max_priority)
        self.root, added = treap_add(self.root, n, priority)
        if added:
            self.size += 1
            self.priorities.add(priority)
        return added

    def remove(self, n):
        self.root, removed = treap_remove(self.root, n)
        if removed:
            self.size -= 1
        return removed

class AvlTree(Bst):
    '''An AVL tree. Does not contain duplicates. Nodes are of type AvlNode.'''
    def __init__(self):
        super().__init__()
        
    def add(self, n):
        self.root, added = avl_add(self.root, n)
        if added:
            self.size += 1
        return added

    def remove(self, n):
        pass
        self.root, removed = avl_remove(self.root, n)
        if removed:
            self.size -= 1
        return removed
    
########## Tree helper functions. ##########
# Work for any type of node above.
    
def tree_string(node, level = 0):
    '''tree_string(node) -> str

    Returns a string representation of the subtree nodeed at node.

    credit: https://stackoverflow.com/questions/20242479/printing-a-tree-data-structure-in-python
    '''
    if not node:
        return '\n'
    prefix = '   '*level
    str = repr(node) + '\n'
    if node.num_children():
        str += prefix + '|_ ' + tree_string(node.left, level+1)
        str += prefix + '|_ ' + tree_string(node.right, level+1)
    return str
    
def tree_size(node):
    '''tree_size(node) -> int
 
    Returns a string representation of the subtree rooted at node.
    '''
    size = 1
    if node is None:
        return 0
    size+=(tree_size(node.right)+tree_size(node.left))
    return size
   
 
def tree_height(node):
    '''tree_height(node) -> int
 
    Returns the height of the subtree rooted at node. Returns -1 if
    node is None.
 
    A node's height is the value of its height attribute, if it
    exists. Otherwise it has to be computed.
 
    See
    - EAFP at https://docs.python.org/3.4/glossary.html
    - https://stackoverflow.com/questions/610883/how-to-know-if-an-object-has-an-attribute-in-python
    '''
    size=1
    if node is None:
        return -1
    elif hasattr(node,'height'):
        return node.height
    else:
        size+=max(tree_height(node.right),tree_height(node.left))
        return size
 
def inorder(n):
    '''inorder(node) -> [node content]
 
    Returns an inorder traversal of the subtree rooted at node; empty
    list if n is None.
    '''
    root=[]
    if n is None:
        return root
    root=[str(n)]
    l=inorder(n.left)
    r=inorder(n.right)
    return l+root+r
   
def preorder(n):
    '''preorder(node) -> [node content] 
    Returns an preorder traversal of the subtree rooted at node; empty
    list if n is None.
    '''
    root=[]
    if n is None:
        return root
    root=[str(n)]
    l=preorder(n.left)
    r=preorder(n.right)
    return root+l+r   
 
def postorder(n):
    '''postorder(node) -> [node content]
    Returns an postorder traversal of the subtree rooted at node;
    empty list if n is None.
    '''
    root=[]
    if n is None:
        return root
    l=postorder(n.left)
    r=postorder(n.right)
    root=[str(n)]
    return l+r+root

def update_height(node):
    '''update_height(node) -> None

    Updates the value of node's height attribute using the height of
    its children.

    Assumes that node has a height attribute.
    '''
    node.height = 1 + max(tree_height(node.left) , tree_height(node.right))

def rotate_left(node):
    '''rotate_left(node) -> node

    Returns the node of the tree obtained by rotating node to the
    left. Updates the height attribute of nodes where necessary and if
    the attribute is present.
    '''
    temp=node.right
    node.right=temp.left
    temp.left=node
    update_height(temp.left)
    update_height(temp)
    
    return temp
    

def rotate_right(node):
    '''rotate_right(node) -> node

    Returns the node of the tree obtained by rotating node to the
    right. Updates the height attribute of nodes where necessary and if
    the attribute is present.
    '''
    temp=node.left
    node.left=temp.right
    temp.right=node
    update_height(temp.right)
    update_height(temp)
    return temp

########## BST helper functions. ##########

def bst_find(node, n):
    '''bst_find(node, int) -> bool

    Returns whether n is contained in the subtree nodeed at
    node. Assumes the subtree to be a BST with no duplicates.
    '''
    if not node:
        return False
    elif (node.data == n):
        return True
    elif (node.data > n):
        return bst_find(node.left,n)
    elif (node.data < n):
        return bst_find(node.right,n)
    else:
        return False
def bst_find_min(node):
    '''bst_find_min(node) -> int

    Returns the smallest value stored in the subtree nodeed at
    node. Assumes the subtree to be a BST with no duplicates.
    '''
    if not node:
        return None
    else:
        while (node.left is not None):
            node=node.left
        return node.data

def bst_add(node, n):
    '''bst_add(node, int) -> (node, bool)

    Returns the result of adding n to the subtree nodeed at
    node. Assumes the subtree to be a BST with no duplicates.

    The first returned value is the node of the tree obtained as a
    result of the addition. The second value indicates whether
    addition succeeded. Addition fails if n is already present in the
    subtree.
    Reference: https://www.geeksforgeeks.org/insertion-binary-tree/
    '''
    bool = True
    if not node:
        node = TreeNode(n)
        return (node,True)
    else:
        if node.data == n:
            return (node,False)
        if node.data > n:
            (node.left, bool) = bst_add(node.left, n)
        else:
            (node.right, bool) = bst_add(node.right, n)
    return (node, bool)
    

def bst_remove(node, n):
    '''bst_remove(node, int) -> (node, bool)

    Returns the result of removing n from the subtree nodeed at
    node. Assumes the subtree to be a BST with no duplicates.

    The first returned value is the node of the tree obtained as a
    result of the removal. The second value indicates whether removal
    succeeded. Removal fails if n is not present in the subtree.
    Reference: https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
    '''
    # Base Case
    bool = False
    if node is None:
        return (node, False)
 
    # If key to be deleted is similiar of node's key then its in left subtree
    if n < node.data:
        (node.left, bool) = bst_remove(node.left, n)
 
    # If key to be deleted is greater than the node's key then its in right subtree
    elif(n > node.data):
        (node.right, bool) = bst_remove(node.right, n)
 
    # If key is same as node's key, then this is the node to be deleted
    else:
        # Node with only one child or no child
        if node.left is None :
            temp = node.right 
            node = None
            return (temp, True) 
             
        elif node.right is None :
            temp = node.left 
            node = None
            return (temp, True)
 
        # Node with two children: Get the inorder successor
        # (smallest in the right subtree)
        temp = bst_find_min(node.right)
 
        # Copy the inorder successor's content to this node
        node.data = temp.data
 
        # Delete the inorder successor
        (node.right, bool) = bst_remove(node.right , temp.data)
 
    return (node, bool) 


########## BST helper functions. ##########

def treap_add(node, n, p):
    temp=None
    #If root node is null, create it
    if node is None:
        node=TreapNode(n,p)
    #If it already exists (duplicate), addition failed
    elif bst_find(node,n) == True:
        return (node,False)
    #If n is greater than root node, insert in right subtree recursively & rotate (as/if required)
    elif (node.data < n):
        node.right = treap_add(node.right,n,p)[0]
        if (node.right.priority < node.priority):
            node = rotate_left(node)
    elif (node.data > n):
        node.left = treap_add(node.left, n, p)[0]
        if (node.left.priority < node.priority):
            node = rotate_right(node)
    return(node,True)
                

 
                            
#SOURCE: https://www.geeksforgeeks.org/treap-set-2-implementation-of-search-insert
 
 
def treap_remove(node, n):
    '''treap_remove(node, int) -> (node, bool)
 
    Returns the result of removing n from the subtree rooted at
    node. Assumes the subtree to be a treap with no duplicate values.
 
    The first returned value is the root of the treap obtained as a
    result of the removal. The second value indicates whether removal
    succeeded. Removal fails if n is not present in the subtree.
    '''
    if node is None:
        return node
    #If n is NOT root
    if (n<node.data):
        node.left=treap_remove(node.left, n)
    elif (n>node.data):
        node.data=treap_remove(node.right, n)
 
    #if n at root, and left is null - make left child the root
    elif (node.left==Null):
        node.right = TreapNode(temp,p)
        remove(node, node.data)
        node=temp
 
    #if n at root, and right is null - make right child the root
    elif (node.right==Null):
        node.left =TreapNode(temp)
        remove(node, node.data)
        node=temp  
    #if n at root, and has both (right/left) children, find maximum and perform rotation accordingly
    elif (node.left.priority<node.right.priority):
        node=rotate_left(node)
        node.left=treap_remove(node.left, n)
    else:
        node=rotate_right(node)
        node.right=treap_remove(node.right, n)
       
    return node, True
#SOURCE: https://www.geeksforgeeks.org/treap-set-2-implementation-of-search-insert-and-delete/
########## AVL helper functions. ##########
        
def avl_balanced(node):
    '''avl_balanced(node) -> bool

    Returns whether the AVL property is satisfied at node. Should work
    for any of the nodes defined above.
    '''
    if not node:
        return
    elif ((abs(tree_height(node.left) - tree_height(node.right)))>1):
        return False
    return True

def avl_left_left(node):
    '''avl_left_left(node) -> node
    
    Returns the node of the tree obtained by resolving a left-left
    case at node.
    '''
    return rotate_right(node)

def avl_right_right(node):
    '''avl_right_right(node) -> node
    
    Returns the node of the tree obtained by resolving a right_right
    case at node.
    '''
    return rotate_left(node)

def avl_left_right(node):
    '''avl_left_right(node) -> node
    
    Returns the node of the tree obtained by resolving a left_right
    case at node.
    '''
    node.left=rotate_left(node.left)
    update_height(node)
    return rotate_right(node)

def avl_right_left(node):
    '''avl_right_left(node) -> node
    
    Returns the node of the tree obtained by resolving a right_left
    case at node.
    '''
    node.right=rotater_right(node.right)
    update_height(node)
    return rotate_left(node)

def avl_add(node, n):
    '''avl_add(node, int) -> (node, bool)

    Returns the result of adding n to the subtree nodeed at
    node. Assumes the subtree to be a valid AVL tree with no
    duplicates.

    The first returned value is the node of the AVL tree obtained as a
    result of the addition. The second value indicates whether
    addition succeeded. Addition fails if n is already present in the
    subtree.

    Reference: https://www.geeksforgeeks.org/avl-tree-set-1-insertion/
    '''
    if not node:
        return (AvlNode(n),True)
    elif node.data == n:
        return (node,False)
    elif (node.data < n):
        ans,val = avl_add(node.right,n)
        if val==True:
            node.right=ans
            update_height(node)
            boolean=True
        else:
            boolean=False
    else:
        ans,val = avl_add(node.left,n)
        if val==True:
            node.left=ans
            update_height(node)
            boolean=True
        else:
            boolean=False
    
    balance = avl_balanced(node)
    if balance == False:      
        bal_avl = tree_height(node.right)-tree_height(node.left)
        
        if bal_avl > 1 and n < node.right.data:
            node = avl_right_left(node)
            
        elif bal_avl < -1 and n > node.left.data:
            node = avl_left_right(node)

        elif bal_avl > 1 and n > node.right.data:
            node = avl_right_right(node)

        elif bal_avl < -1 and n < node.left.data:
            node = avl_left_left(node)
        update_height(node)

    return (node,boolean)

def avl_remove(node, n):
    '''avl_remove(node, int) -> (node, bool)

    Returns the result of removing n from the subtree nodeed at
    node. Assumes the subtree to be a valid AVL tree with no
    duplicates.

    The first returned value is the node of the AVL tree obtained as a
    result of the removal. The second value indicates whether removal
    succeeded. Removal fails if n is not present in the subtree.
    
    Reference: https://www.geeksforgeeks.org/avl-tree-set-2-deletion/
    '''
    
    if not node:
        return (node, False)
    elif n > node.data:
        ans,val= avl_remove(node.right,n)
        if val == True:
            node.right=ans
            update_height(node)
            boolean=True
        else:
            boolean=False
    elif n < node.data:
        ans,val=avl_remove(node.left,n)
        if val==True:
            node.left= ans
            update_height(node)
            boolean=True
        else:
            boolean=False
    
    else:
        if (node.left == None):
            if (node.right == None):
                node = None
            else:
                node = rotate_left(node)
                node,val = avl_remove(node,n)
        elif (node.left and node.right == None ):
            node = rotate_right(node)
            node,val=avl_remove(node,n)
        else:
            curr=node.right
            while curr.left!=None:
                curr=curr.left
            node.data=curr.data
            node.right= avl_remove(node.right,curr.data)[0]
            
        boolean = True
    bal_avl=0
    if node and avl_balanced(node)==False:
        bal_avl=tree_height(node.right)-tree_height(node.left)
        
    if bal_avl>1 and avl_balanced(node.left)==False:
        node = avl_right_left(node)

    elif bal_avl<-1 and avl_balanced(node.left)==False:
        node = avl_left_right(node)
        
    elif bal_avl<-1 and tree_height(node.right)-tree_height(node.left)<=0:
        node = avl_left_left(node)
        
    elif bal_avl>1 and tree_height(node.right)-tree_height(node.left)>=0:
        node = avl_right_right(node)
        
    return (node, boolean)

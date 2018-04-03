from trees import *

lst_add = [34, 82, 26, 60, 11, 18, 82, 55, 48, 76, 94, 55]
lst_rem = [0, 48, 12, 48, 50, 11]
bst_adds = [True, 1, '34\n', True, 2, '34\n|_ \n|_ 82\n', True, 3, '34\n|_ 26\n|_ 82\n', True, 4, '34\n|_ 26\n|_ 82\n   |_ 60\n   |_ \n', True, 5, '34\n|_ 26\n   |_ 11\n   |_ \n|_ 82\n   |_ 60\n   |_ \n', True, 6, '34\n|_ 26\n   |_ 11\n      |_ \n      |_ 18\n   |_ \n|_ 82\n   |_ 60\n   |_ \n', False, 6, '34\n|_ 26\n   |_ 11\n      |_ \n      |_ 18\n   |_ \n|_ 82\n   |_ 60\n   |_ \n', True, 7, '34\n|_ 26\n   |_ 11\n      |_ \n      |_ 18\n   |_ \n|_ 82\n   |_ 60\n      |_ 55\n      |_ \n   |_ \n', True, 8, '34\n|_ 26\n   |_ 11\n      |_ \n      |_ 18\n   |_ \n|_ 82\n   |_ 60\n      |_ 55\n         |_ 48\n         |_ \n      |_ \n   |_ \n', True, 9, '34\n|_ 26\n   |_ 11\n      |_ \n      |_ 18\n   |_ \n|_ 82\n   |_ 60\n      |_ 55\n         |_ 48\n         |_ \n      |_ 76\n   |_ \n', True, 10, '34\n|_ 26\n   |_ 11\n      |_ \n      |_ 18\n   |_ \n|_ 82\n   |_ 60\n      |_ 55\n         |_ 48\n         |_ \n      |_ 76\n   |_ 94\n', False, 10, '34\n|_ 26\n   |_ 11\n      |_ \n      |_ 18\n   |_ \n|_ 82\n   |_ 60\n      |_ 55\n         |_ 48\n         |_ \n      |_ 76\n   |_ 94\n']
avl_adds = [True, 1, '(34, 0)\n', True, 2, '(34, 1)\n|_ \n|_ (82, 0)\n', True, 3, '(34, 1)\n|_ (26, 0)\n|_ (82, 0)\n', True, 4, '(34, 2)\n|_ (26, 0)\n|_ (82, 1)\n   |_ (60, 0)\n   |_ \n', True, 5, '(34, 2)\n|_ (26, 1)\n   |_ (11, 0)\n   |_ \n|_ (82, 1)\n   |_ (60, 0)\n   |_ \n', True, 6, '(34, 2)\n|_ (18, 1)\n   |_ (11, 0)\n   |_ (26, 0)\n|_ (82, 1)\n   |_ (60, 0)\n   |_ \n', False, 6, '(34, 2)\n|_ (18, 1)\n   |_ (11, 0)\n   |_ (26, 0)\n|_ (82, 1)\n   |_ (60, 0)\n   |_ \n', True, 7, '(34, 2)\n|_ (18, 1)\n   |_ (11, 0)\n   |_ (26, 0)\n|_ (60, 1)\n   |_ (55, 0)\n   |_ (82, 0)\n', True, 8, '(34, 3)\n|_ (18, 1)\n   |_ (11, 0)\n   |_ (26, 0)\n|_ (60, 2)\n   |_ (55, 1)\n      |_ (48, 0)\n      |_ \n   |_ (82, 0)\n', True, 9, '(34, 3)\n|_ (18, 1)\n   |_ (11, 0)\n   |_ (26, 0)\n|_ (60, 2)\n   |_ (55, 1)\n      |_ (48, 0)\n      |_ \n   |_ (82, 1)\n      |_ (76, 0)\n      |_ \n', True, 10, '(34, 3)\n|_ (18, 1)\n   |_ (11, 0)\n   |_ (26, 0)\n|_ (60, 2)\n   |_ (55, 1)\n      |_ (48, 0)\n      |_ \n   |_ (82, 1)\n      |_ (76, 0)\n      |_ (94, 0)\n', False, 10, '(34, 3)\n|_ (18, 1)\n   |_ (11, 0)\n   |_ (26, 0)\n|_ (60, 2)\n   |_ (55, 1)\n      |_ (48, 0)\n      |_ \n   |_ (82, 1)\n      |_ (76, 0)\n      |_ (94, 0)\n']
bst_rems = [False, 10, '34\n|_ 26\n   |_ 11\n      |_ \n      |_ 18\n   |_ \n|_ 82\n   |_ 60\n      |_ 55\n         |_ 48\n         |_ \n      |_ 76\n   |_ 94\n', True, 9, '34\n|_ 26\n   |_ 11\n      |_ \n      |_ 18\n   |_ \n|_ 82\n   |_ 60\n      |_ 55\n      |_ 76\n   |_ 94\n', False, 9, '34\n|_ 26\n   |_ 11\n      |_ \n      |_ 18\n   |_ \n|_ 82\n   |_ 60\n      |_ 55\n      |_ 76\n   |_ 94\n', False, 9, '34\n|_ 26\n   |_ 11\n      |_ \n      |_ 18\n   |_ \n|_ 82\n   |_ 60\n      |_ 55\n      |_ 76\n   |_ 94\n', False, 9, '34\n|_ 26\n   |_ 11\n      |_ \n      |_ 18\n   |_ \n|_ 82\n   |_ 60\n      |_ 55\n      |_ 76\n   |_ 94\n', True, 8, '34\n|_ 26\n   |_ 18\n   |_ \n|_ 82\n   |_ 60\n      |_ 55\n      |_ 76\n   |_ 94\n']
avl_rems = [False, 10, '(34, 3)\n|_ (18, 1)\n   |_ (11, 0)\n   |_ (26, 0)\n|_ (60, 2)\n   |_ (55, 1)\n      |_ (48, 0)\n      |_ \n   |_ (82, 1)\n      |_ (76, 0)\n      |_ (94, 0)\n', True, 9, '(34, 3)\n|_ (18, 1)\n   |_ (11, 0)\n   |_ (26, 0)\n|_ (60, 2)\n   |_ (55, 0)\n   |_ (82, 1)\n      |_ (76, 0)\n      |_ (94, 0)\n', False, 9, '(34, 3)\n|_ (18, 1)\n   |_ (11, 0)\n   |_ (26, 0)\n|_ (60, 2)\n   |_ (55, 0)\n   |_ (82, 1)\n      |_ (76, 0)\n      |_ (94, 0)\n', False, 9, '(34, 3)\n|_ (18, 1)\n   |_ (11, 0)\n   |_ (26, 0)\n|_ (60, 2)\n   |_ (55, 0)\n   |_ (82, 1)\n      |_ (76, 0)\n      |_ (94, 0)\n', False, 9, '(34, 3)\n|_ (18, 1)\n   |_ (11, 0)\n   |_ (26, 0)\n|_ (60, 2)\n   |_ (55, 0)\n   |_ (82, 1)\n      |_ (76, 0)\n      |_ (94, 0)\n', True, 8, '(34, 3)\n|_ (18, 1)\n   |_ \n   |_ (26, 0)\n|_ (60, 2)\n   |_ (55, 0)\n   |_ (82, 1)\n      |_ (76, 0)\n      |_ (94, 0)\n']

def test_bst_add():
    tree = Bst()
    assert (tree.size == 0)
    for i,x in enumerate(lst_add):
        adds = bst_adds[3*i:3*i+3]
        assert([tree.add(x), tree.size, tree_string(tree.root)] == adds)

def test_avl_add():
    tree = AvlTree()
    assert (tree.size == 0)
    for i,x in enumerate(lst_add):
        adds = avl_adds[3*i:3*i+3]
        assert([tree.add(x), tree.size, tree_string(tree.root)] == adds)

def test_bst_find():
    tree = Treap()
    [tree.add(x) for x in lst_add]
    a,b = min(lst_add), max(lst_add)
    nums = set(lst_add)
    for _ in range(1000):
        key = random.randint(a,b)
        assert(tree.find(key) == (key in nums))

def test_bst_remove():
    tree = Bst()
    assert(tree.size == 0)
    assert(tree.remove(10) == False)
    [tree.add(x) for x in lst_add]
    for i,x in enumerate(lst_rem):
        rems = bst_rems[3*i:3*i+3]
        assert([tree.remove(x), tree.size, tree_string(tree.root)] == rems)

def test_avl_remove():
    tree = AvlTree()
    assert(tree.size == 0)
    assert(tree.remove(10) == False)
    [tree.add(x) for x in lst_add]
    for i,x in enumerate(lst_rem):
        rems = avl_rems[3*i:3*i+3]
        assert([tree.remove(x), tree.size, tree_string(tree.root)] == rems)

def test_treap():
    tree = Treap()
    [tree.add(x) for x in lst_add]
    stack = [tree.root]
    while stack:
        node = stack.pop()
        if node.left:
            assert(node.priority < node.left.priority)
            stack.append(node.left)
        if node.right:
            assert(node.priority < node.right.priority)
            stack.append(node.right)

def test_traversals():
    tree = Treap()
    [tree.add(x) for x in lst_add]
    keys = [int(key[1:key.find(',')]) for key in inorder(tree.root)]
    assert(keys == sorted(set(lst_add)))
    tree = Bst()
    [tree.add(x) for x in lst_add]
    keys = [int(key) for key in inorder(tree.root)]
    assert(keys == sorted(set(lst_add)))
    lst = ['34', '26', '11', '18', '82', '60', '55', '48', '76', '94']
    assert(preorder(tree.root) == lst)
    lst = ['18', '11', '26', '48', '55', '76', '60', '94', '82', '34']
    assert(postorder(tree.root) == lst)
    

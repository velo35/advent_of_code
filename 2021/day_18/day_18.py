import math


input_file = 0 and 'real.txt' or 'sample.txt'

with open('2021/day_18/input/' + input_file) as f:
    input = f.read()

class Node:
    def __init__(self, left = None, right = None):
        self.parent = None
        self.left = left
        self.right = right
        if left and not isinstance(left, int):
            left.parent = self
        if right and not isinstance(right, int):
            right.parent = self

    def __str__(self):
        return '[' + str(self.left) + ', ' + str(self.right) + ']'

def magnitude(node):
    if not node:
        return 0
    if isinstance(node, int):
        return node
    return 3 * magnitude(node.left) + 2 * magnitude(node.right)
        
def parse_tree(arr):
    left, right = arr[0], arr[1]
    try:
        left = int(left)
    except TypeError:
        left = parse_tree(left)
    
    try:
        right = int(right)
    except TypeError:
        right = parse_tree(right)
    
    return Node(left, right)

def explode_node(node):
    snode = node
    while snode.parent and snode.parent.right != snode:
        snode = snode.parent
    if snode.parent:
        if isinstance(snode.parent.left, int):
            snode.parent.left += node.left
        else:
            rnode = snode.parent.left
            while not isinstance(rnode.right, int):
                rnode = rnode.right
            rnode.right += node.left
        
    snode = node
    while snode.parent and snode.parent.left != snode:
        snode = snode.parent
    if snode.parent:
        if isinstance(snode.parent.right, int):
            snode.parent.right += node.right
        else:
            lnode = snode.parent.right
            while not isinstance(lnode.left, int):
                lnode = lnode.left
            lnode.left += node.right

def explode(node, depth = 0):
    if not isinstance(node, Node):
        return
    explode(node.left, depth + 1)
    explode(node.right, depth + 1)
    
    if depth >= 3:
        if isinstance(node.left, Node):
            explode_node(node.left)
            node.left = 0
        if isinstance(node.right, Node):
            explode_node(node.right)
            node.right = 0
    
def split(node):
    if not isinstance(node, Node):
        return False
    elif isinstance(node.left, int) and node.left >= 10:
        node.left = Node(math.floor(node.left / 2), math.ceil(node.left / 2))
        node.left.parent = node
        return True
    elif split(node.left):
        return True
    elif isinstance(node.right, int) and node.right >= 10:
        node.right = Node(math.floor(node.right / 2), math.ceil(node.right / 2))
        node.right.parent = node
        return True
    elif split(node.right):
        return True
    return False
    
def add(first , second):
    result = Node(first, second)
    explode(result)
    while split(result):
        explode(result)
    return result

snumbers = [parse_tree(eval(x)) for x in input.strip().split('\n')]
value, *rest = snumbers
for v in rest:
    value = add(value, v)
print(value)
print(magnitude(value))



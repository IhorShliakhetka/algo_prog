import os

class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def preorder(self, nodes):
        if self.value != 'N': 
            nodes.append(self.value)
        if self.left: self.left.preorder(nodes)
        if self.right: self.right.preorder(nodes)

    def find_successor(self, target_value):
        nodes = []
        self.preorder(nodes)
        for i in range(len(nodes) - 1):
            if nodes[i] == target_value:
                return nodes[i + 1]
        return None

    def __str__(self):
        grid_width = 200
        grid_height = 60
        grid = [[" " for _ in range(grid_width)] for _ in range(grid_height)]
        cx, cy = 25, 12
        
        def write_str(x, y, text):
            for i, ch in enumerate(str(text)):
                if 0 <= y < grid_height and 0 <= x + i < grid_width:
                    grid[y][x + i] = ch

        write_str(cx, cy, self.value)
        
        def draw_node(node, x, y, is_left_side, y_step):
            dx = -8 if is_left_side else 8
            if node.left:
                nx, ny = x + dx, y + y_step 
                write_str(x + dx//2, y + y_step//2, "/" if is_left_side else "\\")
                write_str(nx, ny, node.left.value)
                draw_node(node.left, nx, ny, is_left_side, max(2, y_step - 1))
                
            if node.right:
                nx, ny = x + dx, y - y_step
                write_str(x + dx//2, y - y_step//2, "\\" if is_left_side else "/")
                write_str(nx, ny, node.right.value)
                draw_node(node.right, nx, ny, is_left_side, max(2, y_step - 1))

        if self.left:
            nx = cx - 5
            for i in range(nx + 2, cx - 1): grid[cy][i] = "-"
            write_str(nx, cy, self.left.value)
            draw_node(self.left, nx, cy, True, 4)
            
        if self.right:
            nx = cx + 6
            for i in range(cx + 3, nx - 1): grid[cy][i] = "-"
            write_str(nx, cy, self.right.value)
            draw_node(self.right, nx, cy, False, 4)

        result_text = []
        for row in grid:
            line = "".join(row).rstrip()
            if line:
                result_text.append(line)
        return "\n".join(result_text)

def build_tree_preorder(iterator):
    try:
        val = next(iterator)
    except StopIteration:
        return None
        
    if val.upper() == 'N': 
        return None
        
    node = BinaryTree(int(val))
    node.left = build_tree_preorder(iterator)
    node.right = build_tree_preorder(iterator)
    
    return node

def build_tree(filename):
    with open(filename, 'r') as f:
        content = f.read()
        full_list = content.split()
        
    iterator = iter(full_list)
    return build_tree_preorder(iterator)


if __name__ == "__main__":
    file = "preorder_tree.txt"


    tree = build_tree(file)

    if tree:
        print(tree)
        
        target = 5
        succ = tree.find_successor(target)
        print(f"\nНаступник для вузла {target} -> {succ}")
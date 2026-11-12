r"""
Assessment 3.3: Non-linear Data Structure
Diagram 1: Binary Tree (BFS and DFS)

        G
       / \
      A   B
     / \   \
    A   S   A
"""

from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    # Breadth-First Search (level by level, uses a queue)
    def bfs(self):
        result = []
        if self.root is None:
            return result

        queue = deque()
        queue.append(self.root)

        while queue:
            current = queue.popleft()
            result.append(current.value)

            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)

        return result

    # Depth-First Search (pre-order: node, left, right)
    def dfs(self, node, result=None):
        if result is None:
            result = []
        if node is None:
            return result

        result.append(node.value)
        self.dfs(node.left, result)
        self.dfs(node.right, result)
        return result


def build_tree():
    root = Node("G")
    root.left = Node("A")
    root.right = Node("B")
    root.left.left = Node("A")
    root.left.right = Node("S")
    root.right.left = Node("A")
    return BinaryTree(root)


if __name__ == "__main__":
    print("GABASA, ANGELITO L.| BSIT 2B")
    input("Please press enter to continue...")
    tree = build_tree()

    print("\n------------------------------------")
    print("Binary Tree Traversal")
    print("BFS:", " - ".join(tree.bfs()))
    print("DFS:", " - ".join(tree.dfs(tree.root)))
    print("------------------------------------")
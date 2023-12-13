# Tree Traversal:
#         1
#       /   \
#      2     3
#     / \
#    4   5

# inorderTraversal: 4 2 5 1 3
# Preorder Traversal: 4 5 2 3 1
# Postorder Traversal: 1 2 4 5 3


class Node:
    def __init__(self, root):
        self.leftChild = None
        self.rightChild = None
        self.data = root


def inorderTraversal(root):
    if root:
        inorderTraversal(root.leftChild)
        print(root.data, end=" ")
        inorderTraversal(root.rightChild)


def preorderTraversal(root):
    if root:
        preorderTraversal(root.leftChild)
        preorderTraversal(root.rightChild)
        print(root.data, end=" ")


def postorderTraversal(root):
    if root:
        print(root.data, end=" ")
        postorderTraversal(root.leftChild)
        postorderTraversal(root.rightChild)


if __name__ == "__main__":
    root = Node(1)
    root.leftChild = Node(2)
    root.rightChild = Node(3)

    root.leftChild.leftChild = Node(4)
    root.leftChild.rightChild = Node(5)

print("Inorder Traversal")
inorderTraversal(root)

print('\n')
print("Preorder Traversal")
preorderTraversal(root)

print('\n')
print("Postorder Traversal")
postorderTraversal(root)
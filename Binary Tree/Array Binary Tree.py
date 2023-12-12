# Example binary tree:
#         A(0)
#       /      \             if (say)root = p
#      b(1)     C(2)         then left = (2*p)+1
#     /   \                  and right = (2*p)+2
#    D(3) E(4)
#                  Complete Binary Tree

tree = [None] * 10


def root(key):
    if tree[0] is not None:
        print("Root node already exist")
    else:
        tree[0] = key


def left(value, parrent):
    if tree[parrent] is None:
        print("Parrent None Missing")
    else:
        tree[(2 * parrent) + 1] = value


def right(value, parrent):
    if tree[parrent] is None:
        print("Parrent Node Missing")
    else:
        tree[(2 * parrent) + 2] = value


def display_tree():
    for i in range(10):
        if tree[i] != None:
            print(tree[i], end="")
        else:
            print("-", end="")
    print()


root('A')
left('B', 0)
right('C', 0)
left('D', 1)
right('E', 1)

display_tree()
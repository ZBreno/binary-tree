from PrettyPrint import PrettyPrintTree


class Node:
    def __init__(self, value):
        self.value = value
        self.smaller = None
        self.bigger = None


class BinaryTree:
    def __init__(self, source):
        self.source = source

    def get_source(self):
        return self.source

    def insert(self, value, node=None):
        nodeSource = node if node else self.get_source()
        newNode = Node(value)

        if (value > nodeSource.value):
            if nodeSource.bigger:
                return self.insert(value, nodeSource.bigger)
            else:
                nodeSource.bigger = newNode
        elif (value < nodeSource.value):
            if nodeSource.smaller:
                return self.insert(value, nodeSource.smaller)
            else:
                nodeSource.smaller = newNode
        else:
            print(f"{value} ja existe")

    def count_nodes(self, node):
        if node is None:
            return 0
        else:
            height_smaller = self.count_nodes(node.smaller)
            height_bigger = self.count_nodes(node.bigger)
            return height_smaller + height_bigger + 1

    def count_leaf(self, node):
        if node is None:
            return 0
        elif (node.smaller is None and node.bigger is None):
            return 1
        else:
            height_smaller = self.count_leaf(node.smaller)
            height_bigger = self.count_leaf(node.bigger)
            return height_smaller + height_bigger

    def calc_height(self, node):
        if node is None:
            return 0
        else:
            height_smaller = self.calc_height(node.smaller)
            height_bigger = self.calc_height(node.bigger)
            return max(height_smaller, height_bigger)+1


ptt = PrettyPrintTree(
    lambda x: [x for x in [x.smaller, x.bigger] if x is not None],
    lambda x: x.value
)
source = Node(5)
tree = BinaryTree(source)

tree.insert(3)
tree.insert(4)
tree.insert(8)
tree.insert(6)
tree.insert(2)
tree.insert(2.2)
tree.insert(2.3)
tree.insert(1)
tree.insert(1.5)
tree.insert(1.6)
tree.insert(7)
tree.insert(9)
tree.insert(7.5)
tree.insert(7.6)
tree.insert(7.7)

ptt(source)

print("\n")
print("-" * 60)
print(
    f"A altura da árvore binária é de comprimento {tree.calc_height(source)}")
print("-" * 60)
print(f"A quantidade de nós da árvore binária é de {tree.count_nodes(source)}")
print("-" * 60)
print(
    f"A quantidade de folhas da árvore binária é de {tree.count_leaf(source)}")

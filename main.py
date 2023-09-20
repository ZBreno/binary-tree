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

    def search_node(self, node):
        if (not node):
            return None

        while node.smaller:
            node = node.smaller

        return node

    def search_smaller(self, value, node, nodeSmaller=None):
        if (not node):
            return nodeSmaller, node
        elif (value > node.value):
            nodeSmaller = node
            value = node.value
            if (node.smaller):
                return self.search_smaller(value, node.smaller, nodeSmaller)
            else:
                return self.search_smaller(value, node.bigger, nodeSmaller)
        elif (value == node.value):
            return self.search_smaller(value, node.smaller)

    def calc_height(self, node):
        if node is None:
            return 0
        else:
            height_smaller = self.calc_height(node.smaller)
            height_bigger = self.calc_height(node.bigger)
            return max(height_smaller, height_bigger)+1

    def delete_node(self, value, node=None, nodePrevious=None):
        nodeSource = node if node else self.get_source()
        if (value > nodeSource.value):
            return self.delete_node(value, nodeSource.bigger, nodeSource)
        elif (value < nodeSource.value):
            return self.delete_node(value, nodeSource.smaller, nodeSource)
        elif (value == nodeSource.value):

            if (nodeSource.smaller == None and nodeSource.bigger == None):
                if (value > nodePrevious.value):
                    nodePrevious.bigger = None
                else:
                    nodePrevious.smaller = None

            elif (nodeSource.smaller == None):
              
                if (nodePrevious.smaller == nodeSource):
                    nodePrevious.smaller = nodeSource.bigger
                else:
                    nodePrevious.bigger = nodeSource.bigger

            elif (nodeSource.bigger == None):
                
                if (nodePrevious.smaller == nodeSource):
                    nodePrevious.smaller = nodeSource.bigger
                else:
                    nodePrevious.bigger = nodeSource.bigger

            elif (nodeSource.bigger and nodeSource.smaller):
                bigger_value = self.search_node(nodeSource.bigger)
                nodeSource.value = bigger_value.value

                return self.delete_node(bigger_value.value, nodeSource.bigger, nodeSource)


ptt = PrettyPrintTree(
    lambda x: [x for x in [x.smaller, x.bigger] if x is not None],
    lambda x: x.value
)
source = Node(51)
tree = BinaryTree(source)

tree.insert(33)
tree.insert(41)
tree.insert(6)
tree.insert(1)
tree.insert(22)
tree.insert(45)
tree.insert(79)
tree.insert(90)
tree.insert(80)
tree.insert(56)
tree.insert(69)
tree.insert(67)
tree.insert(72)
tree.insert(91)
tree.insert(92)
tree.insert(93)
tree.insert(81)
tree.insert(82)
print("antes")
ptt(source)

# print("\n")
# print("-" * 60)
# print(
#     f"A altura da árvore binária é de comprimento {tree.calc_height(source)}")
# print("-" * 60)
# print(f"A quantidade de nós da árvore binária é de {tree.count_nodes(source)}")
# print("-" * 60)
# print(
#     f"A quantidade de folhas da árvore binária é de {tree.count_leaf(source)}")

print("-" * 60)
tree.delete_node(33)
print("depois")

ptt(source)

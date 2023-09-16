class Node:
    def __init__(self, value):
        self.value = value
        self.smaller = None
        self.bigger = None


class BinaryTree:
    def __init__(self, main):
        self.main = main

    def insert(self, value, node = None):
        nodeSource = node if node else self.main
        newNode = Node(value)
        
        if (value > nodeSource.value):
            if nodeSource.bigger:
                return self.insert(value, nodeSource.bigger)
            else:
                nodeSource.bigger = newNode
                return "Inserido!"
        elif (value < nodeSource.value):
            if nodeSource.smaller:
                return self.insert(value, nodeSource.smaller)
            else:
                nodeSource.smaller = newNode
                return "Inserido!"
        else:
            return "Número ja existe"
    
    def count_nodes(self, node):
        pass
    
    def count_leaf(self, node):
        pass
    
    def calc_height(self, node):
        pass
    
    def print_tree(self, node=None, espaco=0):
        raiz = node if node else self.main
        if raiz is None:
            return
        # Espaços em branco para melhor formatação
        espaco += 5
        
        # Processar o nó direito primeiro
        if raiz.bigger:
            self.print_tree(raiz.bigger, espaco)
        
        # Imprimir o nó atual
        print(" " * espaco + str(raiz.value))
        
        # Processar o nó esquerdo
        if raiz.smaller:
            self.print_tree(raiz.smaller, espaco)
            
            
source = Node(5)
tree = BinaryTree(source)

print(tree.insert(3))
print(tree.insert(4))
print(tree.insert(8))
print(tree.insert(6))
print(tree.insert(2))

# print(source.value)
# print(source.bigger.value)
# print(source.bigger.smaller.value)
# print(source.smaller.value)
# print(source.smaller.bigger.value)
# print(source.smaller.smaller.value)
tree.print_tree()
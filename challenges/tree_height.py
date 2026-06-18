from data_structures.node import Node

def tree_height(root: Node | None) -> int:
    if root is None:
        return -1

    altura_esquerda = tree_height(root.get_left_child())
    altura_direita = tree_height(root.get_right_child())
    
    return max(altura_esquerda, altura_direita) + 1
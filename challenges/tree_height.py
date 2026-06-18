from data_structures.node import Node

def tree_height(root: Node | None) -> int:
    # Caso base: se o nó for nulo, a altura é -1
    if root is None:
        return -1
    
    # Descobre a altura da subárvore esquerda e direita recursivamente
    altura_esquerda = tree_height(root.get_left_child())
    altura_direita = tree_height(root.get_right_child())
    
    # A altura do nó atual é a maior altura entre os filhos + 1
    return max(altura_esquerda, altura_direita) + 1
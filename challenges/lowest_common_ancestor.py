from data_structures.node import Node


def lowest_common_ancestor(
    root: Node | None,
    value1: int,
    value2: int,
) -> int:
    if root is None:
        return -1

    no_atual = root

    while no_atual is not None:
        valor_atual = no_atual.get_value()

        if value1 < valor_atual and value2 < valor_atual:
            no_atual = no_atual.get_left_child()
            
        elif value1 > valor_atual and value2 > valor_atual:
            no_atual = no_atual.get_right_child()
            
        else:
            return valor_atual

    return -1

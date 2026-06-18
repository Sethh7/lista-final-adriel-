def has_cycle(graph: dict[str, list[str]]) -> bool:
    no_visitado = set()
    no_caminho = set()

    def busca_em_profundidade(busca):
        no_visitado.add(busca)
        no_caminho.add(busca)

        for vizinho in graph.get(busca,[]):
            if vizinho not in no_visitado:
                if busca_em_profundidade(vizinho):
                    return True
            elif vizinho in no_caminho:
                return True

        no_caminho.remove(busca)
        return False
    
    for busca in graph:
        if busca not in no_visitado:
            if busca_em_profundidade(busca):
                return True
    return False

def group_anagrams(words: list[str]) -> list[list[str]]:
    organizador = {}
    for palavra in words:
        transformacoa_palavra ="".join(sorted(palavra))
        if transformacoa_palavra not in organizador:
            organizador[transformacoa_palavra] = []
                        
        organizador[transformacoa_palavra].append(palavra)
    return list(organizador.values())
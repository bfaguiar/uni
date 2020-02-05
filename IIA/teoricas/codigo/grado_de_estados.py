def grafo_de_estados(no, objectivo):
    abertos = [no]
    fechados = []
    if abertos == []: return False
    fechados.append(abertos.remove(abertos.index(0)))
    if no.getNodeValue() == objectivo:
        return True
    
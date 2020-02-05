class Value():
    def __init__(self):
        pass
    def value(self):
        return self.c
    def __str__(self):
        return str(self.v)

class Constante(Value):
    def __init__(self, c):
        self.c = c
    def __str__(self):
        return str(self.c)

class Variavel(Value):
    def __init__(self):
        pass
    def atribuir(self, e):
        self.v = e.v
    def __str__(self):
        return str(self.v)

class Soma(Value):
    def __init__(self, e1, e2):
        #self.s = float(str(e1)) + float(str(e2))
        assert isinstance(e1, Value)
        assert isinstance(e2, Value)
        self.s = e1.value() + e2.value()

class Produto:
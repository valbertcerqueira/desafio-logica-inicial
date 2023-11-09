class No:
    def __init__(self, x):
        self.chave = x
        self.prox = None

class List:
    def __init__(self):
        self.prim = None

    def lista_vazia(self):
        if self.prim is None:
            return True

    def insert(self, x):
        if x >= 0 and x % 2 == 0:
            p = No(x)
            p.prox = self.prim
            self.prim = p
            return True
        else:
            return False

    def remove_max(self):
        if self.prim == None:
            return

        max_value = -1  # Inicializamos o valor máximo como -1
        prev_max = None
        atual = self.prim

        while atual != None:
            if atual.x > max_value:
                max_value = atual.x
                prev_max = atual
            atual= atual.prox

        if prev_max is not None:
            if prev_max == self.prim:
                self.prim = self.prim.prox
            else:
                prev_max.prox = prev_max.prox.prox


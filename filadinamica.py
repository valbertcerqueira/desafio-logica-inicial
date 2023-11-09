class Fila:
    def __init__(self):
        self.head = 0
        self.elemt = 0
        self.dados = []

    def push(self, x):
        self.dados[self.elemt] = x
        self.elemt += 1

    def delete(self):
        if len(self.dados) == 0:
            return False
        self.head += 1
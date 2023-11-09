class Pilha:
    def __init__(self):
        self.top = 0
        self.dados = []

    def push(self, x):
        self.dados[self.top] = x
        self.top += 1

    def delete(self):
        if self.top == 0:
            return False
        self.top -=1

    def query(self, x):
        n = 0
        if self.top == 0:
            return False
        for i in self.dados:
            if i == x:
                n += 1
        return n
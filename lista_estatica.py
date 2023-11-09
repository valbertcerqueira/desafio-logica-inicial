class lista:
    def __init__(self, maxelemt):
        self.maxelemt = maxelemt
        self.dados = [0] * maxelemt
        self.elemt = 0

    def listavazia(self):
        if self.elemt == 0:
            return True


    def insere(self, x):
        if self.elemt <= self.maxelemt and x >= 0 and x % 2 == 0:
            self.dados[self.elemt] = x
            self.elemt += 1
            return True
        else:
            return False

    def remove(self):
        if self.elemt > 0:
            self.elemt -= 1


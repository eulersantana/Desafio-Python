import random
class PropriedadeModel(object):

    def __init__(self):
        self.custo_venda = 0
        self.valor_aluguel = 0
        self.comprada = False
        self.proprietario = None
        self.ordem = 0

    def definir_custo_venda(self):
        self.custo_venda = int(random.choice(range(100, 1000)))

    def definir_valor_aluguel(self):
        self.valor_aluguel = int(self.custo_venda/2)
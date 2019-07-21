import random
from config import ConfigPartida

class PropriedadeModel(object):

    def __init__(self):
        self.custo_venda = 0
        self.valor_aluguel = 0
        self.comprada = False
        self.proprietario = None
        self.ordem = 0

    def definir_custo_venda(self):
        self.custo_venda = int(random.choice(range(ConfigPartida.VALOR_MIM_PROPRIEDADE, ConfigPartida.VALOR_MAX_PROPRIEDADE)))

    def definir_valor_aluguel(self):
        self.valor_aluguel = int(self.custo_venda/2)
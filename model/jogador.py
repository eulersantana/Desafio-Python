from model.tipo_jogador import TipoJogado

class JogadorModel(object):

    def __init__(self):
        self.saldo = 300
        self.propriedades = []

    def jogador_impulsivo(self):
        self.tipo = TipoJogado.IMPULSIVO

    def jogador_aletorio(self):
        self.tipo = TipoJogado.ALEATORIO

    def jogador_cauteloso(self):
        self.tipo = TipoJogado.CAUTELOSO

    def jogador_exigente(self):
        self.tipo = TipoJogado.EXIGENTE


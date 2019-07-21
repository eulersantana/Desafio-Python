from model.tipo_jogador import TipoJogador

class JogadorModel(object):

    def __init__(self):
        self.saldo = 300
        self.propriedades = []
        self.tipo = 0
        self.posicao_atual = 0

    def jogador_impulsivo(self):
        self.tipo = TipoJogador.IMPULSIVO

    def jogador_aletorio(self):
        self.tipo = TipoJogador.ALEATORIO

    def jogador_cauteloso(self):
        self.tipo = TipoJogador.CAUTELOSO

    def jogador_exigente(self):
        self.tipo = TipoJogador.EXIGENTE


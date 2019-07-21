from model.tipo_jogador import TipoJogador
class AnaliseModel(object):

    def __init__(self):
        # Quantas vezes passou de 1000 rodadas
        self.timeout = 0
        # Numero de vezes que roudou todo tabuleiro até alguem ganhar
        self.turnos = 0
        # ganhadores
        self.ganhadores = []
        #
        self.vencedores = {
            TipoJogador.ALEATORIO.name: 0,
            TipoJogador.IMPULSIVO.name: 0,
            TipoJogador.CAUTELOSO.name: 0,
            TipoJogador.EXIGENTE.name: 0,
        }
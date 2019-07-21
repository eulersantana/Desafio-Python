import  random
from model.propriedade import PropriedadeModel
from model.tipo_jogador import TipoJogador
from model.jogador import JogadorModel


class PartidaBusiness(object):
    @staticmethod
    def criar_tabuleiro():
        tabuleiro = []

        for x in range(1, 41):
            if x % 2 == 0:
                propriedade = PropriedadeModel()
                propriedade.custo_venda()
                propriedade.valor_aluguel()

                casa = {
                    'numero': x,
                    'propriedade': propriedade
                }
                tabuleiro.append(casa)
            else:
                casa = {
                    'numero': x,
                    'propriedade': None
                }
                tabuleiro.append(casa)

        return tabuleiro


    @staticmethod
    def jogadores():
        possibilidade = [x for x in range(1,5)]
        jogadores = []

        while len(possibilidade) > 0:
            selecioando = random.choice(possibilidade)
            jogador = JogadorModel()
            
            if selecioando == TipoJogador.EXIGENTE:
                jogador.jogador_exigente()
            elif selecioando == TipoJogador.CAUTELOSO:
                jogador.jogador_cauteloso()
            elif selecioando == TipoJogador.IMPULSIVO:
                jogador.jogador_impulsivo()
            elif selecioando == TipoJogador.ALEATORIO:
                jogador.jogador_aletorio()

            jogadores.append(jogador)
            possibilidade.remove(selecioando)

        return jogadores

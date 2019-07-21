from model.tipo_jogador import TipoJogado
from utils.uitls import UtilsFunction

class JogoController(object):

    @staticmethod
    def start():
        jogadores = []

        return 1

    def pagar_aluguel(self, jogador, valor_alugel):
        jogador.saldo -= valor_alugel

    def completar_volta(self, jogador):
        jogador.saldo += 100

    def compra_propriedade(self, jogador, propridade):
        if jogador.tipo == TipoJogado.IMPULSIVO:
            propridade.comprada = True
            jogador.propriedades.append(propridade)
        elif jogador.tipo == TipoJogado.EXIGENTE:
            if propridade.valor_aluguel >= 50:
                propridade.comprada = True
                jogador.propriedades.append(propridade)
        elif jogador.tipo == TipoJogado.CAUTELOSO:
            if jogador.saldo - propridade.valor >= 80:
                propridade.comprada = True
                jogador.propriedades.append(propridade)
        elif jogador.tipo == TipoJogado.ALEATORIO:
            if UtilsFunction.compra_or_nao():
                propridade.comprada = True
                jogador.propriedades.append(propridade)

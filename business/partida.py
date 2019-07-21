import  random
from model.propriedade import PropriedadeModel
from model.tipo_jogador import TipoJogador
from model.jogador import JogadorModel
from utils.uitls import UtilsFunction


class PartidaBusiness(object):
    @staticmethod
    def criar_tabuleiro():
        tabuleiro = []

        for x in range(1, 41):
            if x % 2 == 0:
                propriedade = PropriedadeModel()
                propriedade.definir_custo_venda()
                propriedade.definir_valor_aluguel()
                propriedade.ordem = x

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

            if selecioando == TipoJogador.EXIGENTE.value:
                jogador.jogador_exigente()
            elif selecioando == TipoJogador.CAUTELOSO.value:
                jogador.jogador_cauteloso()
            elif selecioando == TipoJogador.IMPULSIVO.value:
                jogador.jogador_impulsivo()
            elif selecioando == TipoJogador.ALEATORIO.value:
                jogador.jogador_aletorio()

            jogadores.append(jogador)
            possibilidade.remove(selecioando)

        return jogadores

    @staticmethod
    def pagar_aluguel(jogador, valor_alugel):
        jogador.saldo -= valor_alugel

    @staticmethod
    def completar_volta( jogador):
        jogador.saldo += 100

    @staticmethod
    def atualizar_posicao(jogador, dado):
        jogador.posicao_atual += dado

    @staticmethod
    def compra_propriedade(jogador, propridade):
        if jogador.tipo == TipoJogador.IMPULSIVO:
            propridade.comprada = True
            jogador.propriedades.append(propridade)
        elif jogador.tipo == TipoJogador.EXIGENTE:
            if propridade.valor_aluguel >= 50:
                propridade.comprada = True
                jogador.propriedades.append(propridade)
        elif jogador.tipo == TipoJogador.CAUTELOSO:
            if jogador.saldo - propridade.custo_venda >= 80:
                propridade.comprada = True
                jogador.propriedades.append(propridade)
        elif jogador.tipo == TipoJogador.ALEATORIO:
            if UtilsFunction.compra_or_nao():
                propridade.comprada = True
                jogador.propriedades.append(propridade)


    @staticmethod
    def analise_partida(analise):
        pass

    @staticmethod
    def contar_timeout(analise):
        analise.timeout += 1

    @staticmethod
    def contar_vencedor(analise, tipo):
        analise.vencedores.update({tipo: analise.vencedores.get(tipo) + 1})

    @staticmethod
    def maior_ganhador(analise):
        maior = {
            'tipo': '',
            'valor': 0
        }
        for key in analise.vencedores:
            if maior.get('valor') < analise.vencedores.get(key):
                maior.update({'tipo': key})
                maior.update({'valor':analise.vencedores.get(key)})

        return maior.get('tipo')

    @staticmethod
    def percentual_vitorias(analise):
        total_vitorias = 0
        for key in analise.vencedores:
            total_vitorias += analise.vencedores.get(key)

        for key in analise.vencedores:
            analise.vencedores.update({key: (analise.vencedores.get(key)/total_vitorias) * 100})
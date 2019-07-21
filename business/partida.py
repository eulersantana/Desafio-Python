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
            if x % 2 != 0:
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
    def devolver_propridade(jogador):
        for propriedade in jogador.propriedades:
            propriedade.comprada = False
            propriedade.proprietario = None

    @staticmethod
    def jogadores():
        possibilidade = [x for x in range(1,5)]
        jogadores = []

        # Selecionando os jogares em ordem aleatoria para iniciar o jogo
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
    def pagar_aluguel(jogador, propriedade):
        jogador.saldo -= propriedade.valor_aluguel
        propriedade.proprietario.saldo += propriedade.valor_aluguel

    @staticmethod
    def completar_volta(jogador):
        jogador.saldo += 100
        jogador.posicao_atual = 0

    @staticmethod
    def atualizar_posicao(jogador, dado):
        jogador.posicao_atual += dado

    @staticmethod
    def compra_propriedade(jogador, propridade):
        if jogador.tipo == TipoJogador.IMPULSIVO:
            # O jogador impulsivo compra qualquer propriedade sobre a qual ele parar
            if jogador.saldo >= propridade.custo_venda:
                jogador.saldo -= propridade.custo_venda
                propridade.comprada = True
                propridade.proprietario = jogador
                jogador.propriedades.append(propridade)

        elif jogador.tipo == TipoJogador.EXIGENTE:
            if jogador.saldo >= propridade.custo_venda:
                # O jogador exigente compra qualquer propriedade, desde que o valor do aluguel dela seja maior do que 50.
                if propridade.valor_aluguel > 50:
                    jogador.saldo -= propridade.custo_venda
                    propridade.comprada = True
                    propridade.proprietario = jogador
                    jogador.propriedades.append(propridade)

        elif jogador.tipo == TipoJogador.CAUTELOSO:
            if jogador.saldo >= propridade.custo_venda:
                # O jogador cauteloso compra qualquer propriedade desde que ele tenha uma reserva de 80 saldo sobrando
                # depois de realizada a compra.
                if jogador.saldo - propridade.custo_venda >= 80:
                    jogador.saldo -= propridade.custo_venda
                    propridade.comprada = True
                    propridade.proprietario = jogador
                    jogador.propriedades.append(propridade)

        elif jogador.tipo == TipoJogador.ALEATORIO:
            if jogador.saldo >= propridade.custo_venda:
                #  O jogador aleatório compra a propriedade que ele parar em cima com probabilidade de 50%.
                if UtilsFunction.compra_or_nao():
                        jogador.saldo -= propridade.custo_venda
                        propridade.comprada = True
                        propridade.proprietario = jogador
                        jogador.propriedades.append(propridade)

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
                maior.update({'valor': analise.vencedores.get(key)})

        return maior.get('tipo')

    @staticmethod
    def percentual_vitorias(analise):
        total_vitorias = 0
        for key in analise.vencedores:
            total_vitorias += analise.vencedores.get(key)

        for key in analise.vencedores:
            analise.vencedores.update({key: (analise.vencedores.get(key)/total_vitorias) * 100})

    @staticmethod
    def calcular_media_turnos(analise, turnos):
        analise.turnos = 0
        for val in turnos:
            analise.turnos += val
        if analise.turnos > 0:
            analise.turnos = analise.turnos/len(turnos)

    @staticmethod
    def resumo_partida(analise, turnos):
        print('Timeout: ' + str(analise.timeout))
        PartidaBusiness.calcular_media_turnos(analise, turnos)
        print('Média de turnos: ' + str(int(analise.turnos)))

        PartidaBusiness.percentual_vitorias(analise)
        vencedores = []
        for key in analise.vencedores:
            vencedores.append({'tipo': key, 'percentural':analise.vencedores.get(key)})

        vencedores = sorted(vencedores, key=lambda x: x.get('percentural'), reverse=True)
        for vencedor in vencedores:
            print(vencedor.get('tipo') + ': ' + str('% 6.2f' % vencedor.get('percentural')) + '%')

        print('Maior Vencedor: ' + PartidaBusiness.maior_ganhador(analise))

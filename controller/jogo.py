from business.partida import PartidaBusiness
from utils.uitls import UtilsFunction
from model.analise import AnaliseModel
from model.tipo_jogador import TipoJogador
class JogoController(object):

    @staticmethod
    def start():
        analise = AnaliseModel()
        simulacoes = 300

        while simulacoes > 0:
            jogadores = PartidaBusiness.jogadores()
            tabuleiro = PartidaBusiness.criar_tabuleiro()
            jogadores_fora = []
            turnos = []
            count_rodadas = 0
            while len(jogadores_fora) < 4 and count_rodadas <= 1000:
                count_rodadas += 1
                dado = UtilsFunction.jogar_dado()

                jogador_atual = jogadores.pop(0)

                if jogador_atual.saldo > 0:
                    if jogador_atual.posicao_atual + dado >= len(tabuleiro):
                        PartidaBusiness.completar_volta(jogador_atual)
                    elif tabuleiro[jogador_atual.posicao_atual + dado].get('propriedade') is not None:
                        propriedade = tabuleiro[jogador_atual.posicao_atual + dado].get('propriedade')
                        if not propriedade.comprada:
                            PartidaBusiness.compra_propriedade(jogador_atual, propriedade)
                        else:
                            PartidaBusiness.pagar_aluguel(jogador_atual, propriedade.valor_aluguel)

                if jogador_atual.saldo < 0:
                    jogadores_fora.append(jogador_atual)
                else:
                    PartidaBusiness.atualizar_posicao(jogador_atual, dado)

                jogadores.append(jogador_atual)

            ganhador = sorted(jogadores, key=lambda jogador: jogador.saldo, reverse=True)

            if count_rodadas >= 1000:
                PartidaBusiness.contar_timeout(analise)
            else:
                turnos.append(count_rodadas)

            PartidaBusiness.contar_vencedor(analise, ganhador[0].tipo.name)

            simulacoes -= 1
        PartidaBusiness.percentual_vitorias(analise)
        print('Timeout: ' + str(analise.timeout))
        print('Média de turnos: ' + str(PartidaBusiness.calcular_media_turnos(turnos)))
        print(TipoJogador.EXIGENTE.name + ': ' + str('% 6.2f' % analise.vencedores.get(TipoJogador.EXIGENTE.name)) + '%')
        print(TipoJogador.CAUTELOSO.name + ': ' + str('% 6.2f' % analise.vencedores.get(TipoJogador.CAUTELOSO.name)) + '%')
        print(TipoJogador.IMPULSIVO.name + ': ' + str('% 6.2f' % analise.vencedores.get(TipoJogador.IMPULSIVO.name)) + '%')
        print(TipoJogador.ALEATORIO.name +': ' + str('% 6.2f' % analise.vencedores.get(TipoJogador.ALEATORIO.name)) + '%')
        print('Maior Vencedor: ' + PartidaBusiness.maior_ganhador(analise))



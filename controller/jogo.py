from config import ConfigPartida
from business.partida import PartidaBusiness
from utils.uitls import UtilsFunction
from model.analise import AnaliseModel
from model.tipo_jogador import TipoJogador
class JogoController(object):

    @staticmethod
    def start():
        analise = AnaliseModel()
        simulacoes = ConfigPartida.MAX_SIMULACOES
        turnos = []
        while simulacoes > 0:
            jogadores = PartidaBusiness.jogadores()
            tabuleiro = PartidaBusiness.criar_tabuleiro()
            jogadores_fora = []
            count_rodadas = 0
            # Execução até restar um unico jogador ou chegar no numero maximo de rodadas
            while len(jogadores_fora) < 4 and count_rodadas <= ConfigPartida.TIMEOUT_PARTIDA:
                count_rodadas += 1
                dado = UtilsFunction.jogar_dado()

                jogador_atual = jogadores.pop(0)

                # Pegando os jogadores que ainda tem saldo
                if jogador_atual.saldo >= 0:
                    # Verificando se o jogador completou o tabuleiro
                    if jogador_atual.posicao_atual + dado > len(tabuleiro):
                        PartidaBusiness.completar_volta(jogador_atual)
                    elif tabuleiro[(jogador_atual.posicao_atual + dado) - 1] is not None and \
                            tabuleiro[(jogador_atual.posicao_atual + dado) - 1].get('propriedade') is not None:
                        propriedade = tabuleiro[(jogador_atual.posicao_atual + dado) - 1].get('propriedade')

                        # Verificando se a propriedade esta disponivel
                        if not propriedade.comprada:
                            PartidaBusiness.compra_propriedade(jogador_atual, propriedade)
                        else:
                            # Pagando aluguel para
                            PartidaBusiness.pagar_aluguel(jogador_atual, propriedade)

                if jogador_atual.saldo < 0:
                    PartidaBusiness.devolver_propridade(jogador_atual)
                    jogadores_fora.append(jogador_atual)
                else:
                    PartidaBusiness.atualizar_posicao(jogador_atual, dado)

                jogadores.append(jogador_atual)

            ganhador = sorted(jogadores, key=lambda jogador: jogador.saldo, reverse=True)

            if ganhador[0].saldo == ganhador[1].saldo:
                if ganhador[0].posicao_atual <= ganhador[1].posicao_atual:
                    copia = ganhador[0]
                    ganhador[0] = ganhador[1]
                    ganhador[1] = copia

            if count_rodadas >= ConfigPartida.TIMEOUT_PARTIDA:
                PartidaBusiness.contar_timeout(analise)
            else:
                turnos.append(count_rodadas)

            PartidaBusiness.contar_vencedor(analise, ganhador[0].tipo.name)

            simulacoes -= 1

        PartidaBusiness.resumo_partida(analise, turnos)


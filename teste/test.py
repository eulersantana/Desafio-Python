import unittest
from controller.jogo import JogoController as jogo
from model.jogador import JogadorModel as jogador
from utils.uitls import UtilsFunction as utils
class TesteJogo(unittest.TestCase):

    def testSaldoJogador(self):
        self.assertEqual(jogador().saldo, 300)

    def testUtilsFuctions(self):
        self.assertIn( utils.jogar_dado(), range(1,7))

if __name__ == '__main__':
    unittest.main()
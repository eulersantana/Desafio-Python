import unittest
from controller.jogo import JogoController

class TesteJogo(unittest.TestCase):
    def test(self):
        self.assertEquals(JogoController.start(), 1)

if __name__ == '__main__':
    unittest.main()
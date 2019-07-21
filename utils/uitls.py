import random
class UtilsFunction(object):
    @staticmethod
    def jogar_dado():
        return random.choice(range(1,7))

    @staticmethod
    def compra_or_nao():
        return True if 1 == random.choice(range(0, 2)) else False
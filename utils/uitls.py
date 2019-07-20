import random
class UtilsFunction(object):
    @staticmethod
    def jogar_dado():
        return random.choice(range(1,7))
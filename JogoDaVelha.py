class Tabuleiro:
     TAMANHO_TABULEIRO = 9
     VAZIO = " "

     def __init__(self):
         self.posicoes = [self.VAZIO] * self.TAMANHO_TABULEIRO

    def _valida_posicao(self, posicao):
        return 0 <= posicao < 9 

    def resetar(self)
        self.posicoes = [' '] * 9
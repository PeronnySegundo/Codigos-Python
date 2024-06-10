class cor:
    VERMELHO = '\033[91m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'
    CIANO = '\033[96m'
    BRANCO = '\033[97m'
    RESET = '\033[0m'

def titulo(mensagem):
    tamanhoLinha = len(mensagem)
    print(cor.AMARELO, '-' * (tamanhoLinha + 40), cor.RESET)
    print(cor.VERDE, ' ' * 19, mensagem, cor.RESET)
    print(cor.AMARELO, '-' * (tamanhoLinha + 40), cor.RESET)
    tamanhoLinha += 40
    global tamanholinha

def tamanhoLinhaFuncao(mensagem):
    tamanhoLinha = len(mensagem)
    print(cor.AMARELO, '-' * (tamanhoLinha + 40), cor.RESET)
    tamanhoLinha += 40
    global tamanholinha

def enter():
    titulo('aperte ENTER para continuar...')
    input('')
    print('\033c')
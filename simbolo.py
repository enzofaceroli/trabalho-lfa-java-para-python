class Simbolo:
    VAZIA = None  # Será inicializado depois

    def __init__(self, simbolo=None):
        """
        Método construtor
        :param simbolo: caractere que representa o símbolo do alfabeto
        """
        self.simbolo = simbolo

    def get_simbolo(self):
        """Obtém o símbolo do alfabeto"""
        return self.simbolo

    def set_simbolo(self, simbolo):
        """Ajusta o símbolo do alfabeto"""
        self.simbolo = simbolo

    def clonar(self):
        """Cria e retorna uma cópia do objeto Simbolo"""
        return Simbolo(self.simbolo)

    def igual(self, outro_simbolo):
        """Verifica se dois símbolos são iguais"""
        return self.simbolo == outro_simbolo.get_simbolo()

    def __str__(self):
        """Retorna a representação em string do símbolo"""
        return str(self.simbolo)

# Inicializando o símbolo vazio
Simbolo.VAZIA = Simbolo('E')
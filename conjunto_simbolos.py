class ConjuntoSimbolo:
    def __init__(self):
        """Inicializa um conjunto de símbolos"""
        self.elementos = set()

    def vazio(self):
        """Verifica se o conjunto está vazio"""
        return not self.elementos

    def limpar(self):
        """Limpa o conjunto de símbolos"""
        self.elementos.clear()

    def inclui(self, elemento):
        """Inclui um elemento no conjunto"""
        self.elementos.add(elemento)

    def pertence(self, elemento):
        """Verifica se um elemento pertence ao conjunto"""
        return any(simbolo.igual(elemento) for simbolo in self.elementos)

    def uniao(self, outro):
        """Realiza a união entre dois conjuntos"""
        novo_conjunto = self.clonar()
        for simbolo in outro.get_elementos():
            if not novo_conjunto.pertence(simbolo):
                novo_conjunto.inclui(simbolo.clonar())
        return novo_conjunto

    def intersecao(self, outro):
        """Realiza a interseção entre dois conjuntos"""
        novo_conjunto = ConjuntoSimbolo()
        for simbolo in outro.get_elementos():
            if self.pertence(simbolo):
                novo_conjunto.inclui(simbolo.clonar())
        return novo_conjunto

    def clonar(self):
        """Cria e retorna uma cópia do conjunto"""
        novo_conjunto = ConjuntoSimbolo()
        for simbolo in self.elementos:
            novo_conjunto.inclui(simbolo.clonar())
        return novo_conjunto

    def igual(self, outro):
        """Verifica se dois conjuntos são iguais"""
        return self.elementos == outro.get_elementos()

    def _str_(self):
        """Retorna a representação em string do conjunto"""
        return "{" + ", ".join(str(simbolo) for simbolo in self.elementos) + "}"

    def get_elementos(self):
        """Retorna os elementos do conjunto"""
        return self.elementos

    def remover_elemento(self, elemento):
        """Remove um elemento do conjunto"""
        self.elementos.discard(elemento)
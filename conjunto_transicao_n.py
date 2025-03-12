class ConjuntoTransicaoN:
    def _init_(self):
        """Inicializa um conjunto de transições não determinísticas"""
        self.elementos = set()

    def vazio(self):
        """Verifica se o conjunto está vazio"""
        return not self.elementos

    def inclui(self, elemento):
        """Inclui um elemento no conjunto"""
        self.elementos.add(elemento.clonar())

    def pertence(self, elemento):
        """Verifica se um elemento pertence ao conjunto"""
        return any(transicao.igual(elemento) for transicao in self.elementos)

    def uniao(self, outro):
        """Realiza a união entre dois conjuntos"""
        novo_conjunto = self.clonar()
        for transicao in outro.get_elementos():
            if not novo_conjunto.pertence(transicao):
                novo_conjunto.inclui(transicao.clonar())
        return novo_conjunto

    def intersecao(self, outro):
        """Realiza a interseção entre dois conjuntos"""
        novo_conjunto = ConjuntoTransicaoN()
        for transicao in outro.get_elementos():
            if self.pertence(transicao):
                novo_conjunto.inclui(transicao.clonar())
        return novo_conjunto

    def clonar(self):
        """Cria e retorna uma cópia do conjunto"""
        novo_conjunto = ConjuntoTransicaoN()
        for transicao in self.elementos:
            novo_conjunto.inclui(transicao.clonar())
        return novo_conjunto

    def igual(self, outro):
        """Verifica se dois conjuntos são iguais"""
        return self.elementos == outro.get_elementos()

    def _str_(self):
        """Retorna a representação em string do conjunto"""
        return "{" + ", ".join(str(transicao) for transicao in self.elementos) + "}"

    def get_elementos(self):
        """Retorna os elementos do conjunto"""
        return self.elementos

    def remover_elemento(self, elemento):
        """Remove um elemento do conjunto"""
        self.elementos.discard(elemento)
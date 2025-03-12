class ConjuntoEstados:
    def __init__(self):
        self.elementos = set()

    def vazio(self):
        return len(self.elementos) == 0

    def limpar(self):
        self.elementos.clear()

    def inclui(self, elemento):
        self.elementos.add(elemento.clonar())

    def pertence(self, elemento):
        return any(estado.igual(elemento) for estado in self.elementos)

    def retorna_igual(self, elemento):
        for estado in self.elementos:
            if estado.igual(elemento):
                return estado
        return None

    def uniao(self, ce):
        novo_conjunto = self.clonar()
        for estado in ce.get_elementos():
            if not novo_conjunto.pertence(estado):
                novo_conjunto.inclui(estado.clonar())
        return novo_conjunto

    def intersecao(self, ce):
        novo_conjunto = ConjuntoEstados()
        for estado in ce.get_elementos():
            if self.pertence(estado):
                novo_conjunto.inclui(estado.clonar())
        return novo_conjunto

    def clonar(self):
        novo_conjunto = ConjuntoEstados()
        for estado in self.elementos:
            novo_conjunto.inclui(estado.clonar())
        return novo_conjunto

    def igual(self, ce):
        return all(self.pertence(e) for e in ce.get_elementos()) and all(ce.pertence(e) for e in self.elementos)

    def _str_(self):
        elementos_str = ", ".join(str(e) for e in self.elementos)
        return "{" + elementos_str + "}"

    def get_elementos(self):
        return self.elementos

    def size(self):
        return len(self.elementos)

    def remover_elemento(self, e):
        self.elementos.discard(e)
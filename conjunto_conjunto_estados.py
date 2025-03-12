from conjunto_estados import ConjuntoEstados

class ConjuntoConjuntoEstados:
    def __init__(self):
        self.elementos = set()

    def vazio(self):
        return len(self.elementos) == 0

    def limpar(self):
        self.elementos.clear()

    def inclui(self, elemento):
        self.elementos.add(elemento.clonar())

    def pertence(self, elemento):
        return any(conjunto.igual(elemento) for conjunto in self.elementos)

    def uniao(self, cce):
        novo_conjunto = self.clonar()
        for conjunto_estados in cce.get_elementos():
            if not novo_conjunto.pertence(conjunto_estados):
                novo_conjunto.inclui(conjunto_estados.clonar())
        return novo_conjunto

    def intersecao(self, cce):
        novo_conjunto = ConjuntoConjuntoEstados()
        for conjunto_estados in cce.get_elementos():
            if self.pertence(conjunto_estados):
                novo_conjunto.inclui(conjunto_estados.clonar())
        return novo_conjunto

    def clonar(self):
        novo_conjunto = ConjuntoConjuntoEstados()
        for conjunto_estados in self.elementos:
            novo_conjunto.inclui(conjunto_estados.clonar())
        return novo_conjunto

    def igual(self, cce):
        aux = cce.clonar()
        for conjunto_estados in aux.get_elementos():
            if not self.pertence(conjunto_estados):
                return False
        aux = self.clonar()
        for conjunto_estados in aux.get_elementos():
            if not cce.pertence(conjunto_estados):
                return False
        return True

    def get_elementos(self):
        return self.elementos

    def remover_elemento(self, ce):
        self.elementos.discard(ce)

    def uniao_interna(self):
        novo = ConjuntoEstados()
        for conjunto in self.elementos:
            novo = novo.uniao(conjunto)
        return novo.clonar()

    def _str_(self):
        return "{" + ",".join(str(e) for e in self.elementos) + "}"
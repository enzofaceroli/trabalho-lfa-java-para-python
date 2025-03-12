class ConjuntoTransicaoD:
    """
    Classe que representa um conjunto de transições determinísticas de um autômato
    """
    
    def __init__(self):
        self.elementos = set()
    
    def vazio(self):
        return len(self.elementos) == 0
    
    def limpar(self):
        self.elementos.clear()
    
    def inclui(self, elemento):
        self.elementos.add(elemento.clonar())
    
    def pertence(self, elemento):
        return any(transicao.igual(elemento) for transicao in self.elementos)
    
    def uniao(self, outro_conjunto):
        novo_conjunto = self.clonar()
        for transicao in outro_conjunto.elementos:
            if not novo_conjunto.pertence(transicao):
                novo_conjunto.inclui(transicao)
        return novo_conjunto
    
    def intersecao(self, outro_conjunto):
        novo_conjunto = ConjuntoTransicaoD()
        for transicao in outro_conjunto.elementos:
            if self.pertence(transicao):
                novo_conjunto.inclui(transicao)
        return novo_conjunto
    
    def clonar(self):
        novo_conjunto = ConjuntoTransicaoD()
        for transicao in self.elementos:
            novo_conjunto.inclui(transicao)
        return novo_conjunto
    
    def igual(self, cce):
        return self.elementos == cce.get_elementos()
    
    def __str__(self):
        return "{" + ", ".join(str(transicao) for transicao in self.elementos) + "}"
    
    def get_elementos(self):
        return self.elementos
    
    def remover_elemento(self, transicao):
        self.elementos.discard(transicao)
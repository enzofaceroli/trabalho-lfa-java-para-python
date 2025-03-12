class TransicaoD:
    """
    Classe que representa a função de transição de um autômato finito determinístico
    """
    
    def __init__(self, origem=None, destino=None, simbolo=None):
        self.origem = origem.clonar() if origem else None
        self.destino = destino.clonar() if destino else None
        self.simbolo = simbolo.clonar() if simbolo else None
    
    def get_destino(self):
        return self.destino.clonar() if self.destino else None
    
    def set_destino(self, destino):
        self.destino = destino.clonar()
    
    def get_origem(self):
        return self.origem.clonar() if self.origem else None
    
    def set_origem(self, origem):
        self.origem = origem.clonar()
    
    def get_simbolo(self):
        return self.simbolo.clonar() if self.simbolo else None
    
    def set_simbolo(self, simbolo):
        self.simbolo = simbolo.clonar()
    
    def clonar(self):
        return TransicaoD(self.origem, self.destino, self.simbolo)
    
    def igual(self, transicao):
        return (
            self.destino.igual(transicao.get_destino()) and
            self.origem.igual(transicao.get_origem()) and
            self.simbolo.igual(transicao.get_simbolo())
        )
    
    def _str_(self):
        return f"({self.origem}, {self.simbolo}, {self.destino})"

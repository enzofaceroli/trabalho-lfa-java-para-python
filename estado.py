class Estado:
    """
    Classe que representa um estado de um autômato
    """
    
    def _init_(self, nome=""):
        self.nome = nome
    
    def get_nome(self):
        return self.nome
    
    def set_nome(self, nome):
        self.nome = nome
    
    def clonar(self):
        return Estado(self.nome)
    
    def igual(self, estado):
        return self.nome == estado.get_nome()
    
    def _str_(self):
        return self.nome
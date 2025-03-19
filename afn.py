from simbolo import Simbolo

class AFN:
    def __init__(self, simbolos=None, estados=None, funcao_programa=None, estado_inicial=None, estados_finais=None):
        if simbolos is None:
            simbolos = set()
        if estados is None:
            estados = set()
        if funcao_programa is None:
            funcao_programa = []
        if estados_finais is None:
            estados_finais = set()
        
        self.simbolos = simbolos.copy()
        self.estados = estados.copy()
        self.funcao_programa = funcao_programa.copy()
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais.copy()
    
    def get_estado_inicial(self):
        return self.estado_inicial
    
    def set_estado_inicial(self, estado_inicial):
        self.estado_inicial = estado_inicial
    
    def get_estados(self):
        return self.estados.copy()
    
    def set_estados(self, estados):
        self.estados = estados.copy()
    
    def get_estados_finais(self):
        return self.estados_finais.copy()
    
    def set_estados_finais(self, estados_finais):
        self.estados_finais = estados_finais.copy()
    
    def get_funcao_programa(self):
        return self.funcao_programa.copy()
    
    def set_funcao_programa(self, funcao_programa):
        self.funcao_programa = funcao_programa.copy()
    
    def get_simbolos(self):
        return self.simbolos.copy()
    
    def set_simbolos(self, simbolos):
        self.simbolos = simbolos.copy()
    
    def clonar(self):
        return AFN(self.simbolos, self.estados, self.funcao_programa, self.estado_inicial, self.estados_finais)
    
    def _str_(self):
        return f"({self.simbolos}, {self.estados}, {self.funcao_programa}, {self.estado_inicial}, {self.estados_finais})"
        
    def p(self, estado, simbolo):
        for transicao in self.funcao_programa:
            if transicao["origem"] == estado and transicao["simbolo"].igual(simbolo):  # Comparação correta de Simbolo
                return transicao["destino"]
        return set()  # Retorna um conjunto vazio se não houver transição
        
    def pe(self, estados, palavra):
        if not palavra:
            return estados
        novo_estados = set()
        simbolo = palavra[0]
        for estado in estados:
            novo_estados.update(self.p(estado, simbolo))  # Processa a transição
        return self.pe(novo_estados, palavra[1:])  # Recursão para o próximo símbolo
        
    def aceita(self, palavra):
        estados_atuais = {self.estado_inicial}
        estados_finais = self.pe(estados_atuais, [Simbolo(c) for c in palavra])  # Converte cada caractere em Simbolo
        return any(estado in self.estados_finais for estado in estados_finais)
        
    def to_xml(self, filename):
        with open(f"{filename}.xml", "w") as file:
            file.write("<AFN>\n")
            file.write("\t<simbolos>\n")
            for simbolo in self.simbolos:
                file.write(f"\t\t<elemento valor=\"{str(simbolo)}\"/>\n")  # Converte Simbolo para string
            file.write("\t</simbolos>\n\n")
            
            file.write("\t<estados>\n")
            for estado in self.estados:
                file.write(f"\t\t<elemento valor=\"{str(estado)}\"/>\n")  # Converte Estado para string
            file.write("\t</estados>\n\n")
            
            file.write("\t<estadosFinais>\n")
            for estado in self.estados_finais:
                file.write(f"\t\t<elemento valor=\"{str(estado)}\"/>\n")  # Converte Estado para string
            file.write("\t</estadosFinais>\n\n")
            
            file.write("\t<funcaoPrograma>\n")
            for transicao in self.funcao_programa:
                file.write(f"\t\t<elemento origem=\"{str(transicao['origem'])}\" destino=\"{str(transicao['destino'])}\" simbolo=\"{str(transicao['simbolo'])}\"/>\n")  # Converte Simbolo e Estado para string
            file.write("\t</funcaoPrograma>\n\n")
            
            file.write(f"\t<estadoInicial valor=\"{str(self.estado_inicial)}\"/>\n\n")  # Converte Estado para string
            file.write("</AFN>")
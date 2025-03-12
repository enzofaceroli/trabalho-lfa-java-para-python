import xml.etree.ElementTree as ET

class AFD:
    def _init_(self, simbolos=None, estados=None, funcao_programa=None, estado_inicial=None, estados_finais=None):
        self.simbolos = simbolos.copy() if simbolos else set()
        self.estados = estados.copy() if estados else set()
        self.funcao_programa = funcao_programa.copy() if funcao_programa else {}
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais.copy() if estados_finais else set()
    
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
        return AFD(self.simbolos, self.estados, self.funcao_programa, self.estado_inicial, self.estados_finais)
    
    def _str_(self):
        return f'({self.simbolos}, {self.estados}, {self.funcao_programa}, {self.estado_inicial}, {self.estados_finais})'
    
    def ler(self, path_arquivo):
        tree = ET.parse(path_arquivo)
        root = tree.getroot()
        
        for elemento in root.findall("simbolos/elemento"):
            self.simbolos.add(elemento.get("valor"))
        
        for elemento in root.findall("estados/elemento"):
            self.estados.add(elemento.get("valor"))
        
        for elemento in root.findall("estadosFinais/elemento"):
            self.estados_finais.add(elemento.get("valor"))
        
        self.estado_inicial = root.find("estadoInicial").get("valor")
        
        for elemento in root.findall("funcaoPrograma/elemento"):
            origem = elemento.get("origem")
            destino = elemento.get("destino")
            simbolo = elemento.get("simbolo")
            self.funcao_programa[(origem, simbolo)] = destino
    
    def processar(self, estado, simbolo):
        return self.funcao_programa.get((estado, simbolo))
    
    def processar_palavra(self, estado, palavra):
        estado_atual = estado
        for simbolo in palavra:
            estado_atual = self.processar(estado_atual, simbolo)
            if estado_atual is None:
                return None
        return estado_atual
    
    def aceita(self, palavra):
        return self.processar_palavra(self.estado_inicial, palavra) in self.estados_finais
    
    def to_xml(self, filename):
        root = ET.Element("AFD")
        
        simbolos_elem = ET.SubElement(root, "simbolos")
        for s in self.simbolos:
            ET.SubElement(simbolos_elem, "elemento", valor=s)
        
        estados_elem = ET.SubElement(root, "estados")
        for e in self.estados:
            ET.SubElement(estados_elem, "elemento", valor=e)
        
        estados_finais_elem = ET.SubElement(root, "estadosFinais")
        for ef in self.estados_finais:
            ET.SubElement(estados_finais_elem, "elemento", valor=ef)
        
        funcao_programa_elem = ET.SubElement(root, "funcaoPrograma")
        for (origem, simbolo), destino in self.funcao_programa.items():
            ET.SubElement(funcao_programa_elem, "elemento", origem=origem, destino=destino, simbolo=simbolo)
        
        ET.SubElement(root, "estadoInicial", valor=self.estado_inicial)
        
        tree = ET.ElementTree(root)
        tree.write(filename + ".xml", encoding="utf-8", xml_declaration=True)
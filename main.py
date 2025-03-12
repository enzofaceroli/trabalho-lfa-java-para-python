from estado import Estado
from simbolo import Simbolo
from conjunto_estados import ConjuntoEstados
from conjunto_simbolos import ConjuntoSimbolo
from conjunto_transicao_n import ConjuntoTransicaoN
from conjunto_transicao_d import ConjuntoTransicaoD
from conjunto_conjunto_estados import ConjuntoConjuntoEstados
from afn import AFN
from afd import AFD

def testar_afn():
    print("Testando AFN...")
    
    q0 = Estado("q0")
    q1 = Estado("q1")
    q2 = Estado("q2")
    
    simbolos = {Simbolo("a"), Simbolo("b")}
    estados = {q0, q1, q2}
    transicoes = [
        {"origem": q0, "simbolo": Simbolo("a"), "destino": {q0, q1}},
        {"origem": q1, "simbolo": Simbolo("b"), "destino": {q2}},
    ]
    
    afn = AFN(simbolos, estados, transicoes, q0, {q2})
    
    print("AFN criado com sucesso!")
    print("Aceita 'ab':", afn.aceita("ab"))  # Deve retornar True
    print("Aceita 'aa':", afn.aceita("aa"))  # Deve retornar False
    
    afn.to_xml("build")
    print("Arquivo XML gerado para o AFN!\n")

def testar_afd():
    print("Testando AFD...")
    
    q0 = Estado("q0")
    q1 = Estado("q1")
    q2 = Estado("q2")
    
    simbolos = {Simbolo("a"), Simbolo("b")}
    estados = {q0, q1, q2}
    transicoes = {
        (q0, Simbolo("a")): q1,
        (q1, Simbolo("b")): q2,
        (q2, Simbolo("a")): q1,
    }
    
    afd = AFD(simbolos, estados, transicoes, q0, {q2})
    
    print("AFD criado com sucesso!")
    print("Aceita 'ab':", afd.aceita("ab"))  # Deve retornar True
    print("Aceita 'aba':", afd.aceita("aba"))  # Deve retornar True
    print("Aceita 'aab':", afd.aceita("aab"))  # Deve retornar False
    
    afd.to_xml("build")
    print("Arquivo XML gerado para o AFD!\n")

def main():
    # Criando estados
    q0 = Estado("q0")
    q1 = Estado("q1")
    q2 = Estado("q2")
    
    # Criando conjunto de estados
    ce1 = ConjuntoEstados()
    ce1.inclui(q0)
    ce1.inclui(q1)
    
    ce2 = ConjuntoEstados()
    ce2.inclui(q1)
    ce2.inclui(q2)
    
    # Criando conjunto de conjuntos de estados
    cce = ConjuntoConjuntoEstados()
    cce.inclui(ce1)
    cce.inclui(ce2)
    
    print("Conjunto de Conjuntos de Estados:")
    print(cce)
    
    # Criando símbolos
    a = Simbolo("a")
    b = Simbolo("b")
    
    # Criando conjunto de símbolos
    cs = ConjuntoSimbolo()
    cs.inclui(a)
    cs.inclui(b)
    
    print("Conjunto de Símbolos:")
    print(cs)
    
    # Testando operações com estados
    print("União de conjuntos de estados:")
    print(ce1.uniao(ce2))
    
    print("Interseção de conjuntos de estados:")
    print(ce1.intersecao(ce2))
    
    # Testando clonagem
    ce_clone = ce1.clonar()
    print("Clone do Conjunto de Estados:")
    print(ce_clone)
    
    # Testando igualdade
    print("Os conjuntos de estados são iguais?")
    print(ce1.igual(ce_clone))
    
    testar_afn()
    testar_afd()

if _name_ == "_main_":
    main()
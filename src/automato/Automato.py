from collections import deque

class Automato:
    """Implementa um automato finito determinístico (AFD) que obedece a 
    seguinte definição:
    M = (Q, Σ, δ, q0, F)
    Q: Conjunto finito de estados
    Σ: Alfabeto
    δ: Função de transição
    q0: Estado inicial
    F: Conjunto de estados finais
    """

    def __init__(self, conj_todos_estados, alfabeto, transicoes,
                estado_inicial, conj_estados_finais):
        self.estados: set = conj_todos_estados
        self.alfabeto: set = alfabeto
        # self.transicoes = transicoes
        self.estado_inicial = estado_inicial
        self.estados_finais = conj_estados_finais
        self.fita = list()
        # self.cursor = 0
        self.maquina_estados: MaquinaEstados = MaquinaEstados(transicoes, self.estado_inicial, self.estados_finais)


    def __repr__(self) -> str:
        return f"""\
        M = (Q, Σ, δ, q0, F)
        Q: {{{','.join(estados)}}}
        Σ: {{{self.alfabeto}}}
        δ: {self.maquina_estados.transicao}
        q0: {self.estado_inicial}
        F: {self.estados_finais}
        """
    
    def __eq__(self, o: Automato) -> bool:
        """Retorna True se os dois automatos forem equivalentes."""
        
        pass

    def reconhecer_cadeia(self, cadeia) -> bool:
        """Recebe uma cadeia de caracteres e retorna True se a cadeia 
        for aceita pelo automato.
        """

        return self.maquina_estados.reconhecer_cadeia(cadeia)



#Maquina de estados
class MaquinaEstados():
    """Classe que implementa uma máquina de estados finitos 
    determinística por composição da classe Automato.
    """
    
    def __init__(self, funcao_de_transicao, estado_inicial, estados_finais):
        self.transicao = funcao_de_transicao
        self.estados_finais = estados_finais
        self.estado_inical = estado_inicial
        self.__estado_atual = estado_inicial
        self.cadeia_restante = None
        self.posicao_cursor = 0
    
    # Opcao com recurcao
    def reconhecer_cadeia(self, cadeia):
        """Reconhece uma cadeia inteira na fita, de acordo com a 
        função de transição.
        """
        resultado = False
        if (self.__estado_atual, cadeia[0]) in self.transicao.keys():
            self.__estado_atual = self.transicao[(self.__estado_atual, cadeia[0])]
            self.cadeia_restante = cadeia[1:]
            if self.cadeia_restante == "":
                return True if self.__estado_atual in self.estados_finais else False
            else:
                resultado = self.reconhecer_cadeia(self.cadeia_restante)
        else:            
            raise KeyError("Transicao nao definida")
        self.__estado_atual = self.estado_inical
        return resultado

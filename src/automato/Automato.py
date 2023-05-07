from collections import deque
from itertools import accumulate


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
    
    estados_finitos: set[str]
    alfabeto: set[str]
    transicoes: dict[dict[str, str]]
    estado_inicial: str
    conj_estados_finais: set[str]
    fita: deque[str]

    def __init__(self, estados_finitos, alfabeto, transicoes,
                estado_inicial, conj_estados_finais):
        self.estados_finitos: set = estados_finitos
        self.alfabeto: set = alfabeto
        self.transicoes = transicoes
        self.estado_inicial = estado_inicial
        self.estados_finais = conj_estados_finais
        self.fita = deque()
        self.cursor = 0
        self.maquina_estados: MaquinaEstados = MaquinaEstados(self)

    def __repr__(self) -> str:
        return f"""\
        M = (Q, Σ, δ, q0, F)
        Q: {{{','.join(self.estados_finitos)}}}
        Σ: {{{self.alfabeto}}}
        δ: {self.maquina_estados.transicao}
        q0: {self.estado_inicial}
        F: {self.estados_finais}\
        """
    
    def __eq__(self, o: "Automato") -> bool:
        """Retorna True se os dois automatos forem equivalentes."""
        # Aqui é preciso aplicar a técnica de minimização em ambos 
        # automatos, o que implica implementar 1. os algoritmos de remoção
        # de transições em vazio; 2. de remoção de não-determinismos;
        # 3. de remoção de estados inúteis ou inacessíveis, nesta ordem.
        #
        # minimo_self = self.rm_transicoes_vazio().rm_nao_determinismo().rm_estados_inuteis()
        # minimo_o = o.rm_transicoes_vazio().rm_nao_determinismo().rm_estados_inuteis()
        pass

    def escrever_fita(self, cadeia: str) -> None:
        """Escreve uma cadeia de caracteres na fita."""
        self.fita.clear()
        self.fita = deque(cadeia)
        self.fita.append("\0")
    
    def ler_celula(self) -> str:
        """Retorna o conteudo da celula atual da fita."""
        self.cursor += 1
        return self.fita.pop()

    def reconhecer_cadeia(self, cadeia) -> bool:
        """Recebe uma cadeia de caracteres e retorna True se a cadeia 
        for aceita pelo automato.
        """
        return self.maquina_estados.reconhecer_cadeia(cadeia)
    
    def rm_transicoes_vazio(self) -> "Automato":
        """Retorna um novo automato sem transições em vazio."""
        # TODO
        pass

    def rm_nao_determinismo(self) -> "Automato":
        """Retorna um novo automato sem não-determinismos."""
        # TODO
        pass

    def rm_estados_inuteis(self) -> "Automato":
        """Retorna um novo automato sem estados inuteis."""
        # TODO
        pass


#Maquina de estados
class MaquinaEstados():
    """Classe que implementa uma máquina de estados finitos 
    determinística por composição da classe Automato.
    """
    
    funcao_transicao: dict[dict[str, str]]
    estado_inicial: str
    estados_finais: set[str]

    def __init__(self, automato: Automato):
        self.transicao = automato.transicoes  # delta(p, rho) -> q
        self.estados_finais = automato.estados_finais
        self.estado_inical = automato.estado_inicial
        self.__estado_atual = automato.estado_inicial
        self.cadeia_restante = None
        self.posicao_cursor = 0
    
    def aplicar_transicao(self, simbolo):
        """Aplica a função de transição δ(p, σ) -> q."""
        self.__estado_atual = self.transicao[self.__estado_atual][simbolo]

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

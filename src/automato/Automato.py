from collections import deque


class Automato:
    """Implementa um automato finito determinístico (AFD) que obedece a 
    seguinte definição:
    M = (Q, Σ, δ, q0, F)
    Q: Conjunto finito de estados
    Σ: Alfabeto
    δ: Função de transição
    q0: Estado inicial
    F: Conjunto de estados finai
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
        # 3. de remoção de estados inúteis ou inacessíveis, e o
        # algoritmo de minimização, nesta ordem.
        #
        # minimo_self = self.rm_transicoes_vazio().rm_nao_determinismo().rm_estados_inuteis()
        # minimo_o = o.rm_transicoes_vazio().rm_nao_determinismo().rm_estados_inuteis()
        pass

    def escrever_fita(self, cadeia: str) -> None:
        """Escreve uma cadeia de caracteres na fita."""
        self.fita.clear()
        self.fita = deque(cadeia)

    def reconhecer_cadeia_alt(self, cadeia: str):
        """Reconhece uma cadeia de caracteres na fita usando uma
        estrutura do tipo fila (deque).
        """
        self.maquina_estados.resetar()    
        self.escrever_fita(cadeia)
        self.maquina_estados.gravar_movimento(self.fita)
        while self.fita:
            simbolo = self.fita.popleft()
            try:
                self.maquina_estados.config_seguinte(simbolo)
                self.maquina_estados.gravar_movimento(self.fita)
            except KeyError:
                return False
        estado_parada = self.maquina_estados.estado_atual
        return bool(estado_parada in self.estados_finais)
    
    def rm_transicoes_vazio(self) -> "Automato":
        """Remove transições em vazio do automato."""
        # TODO
        pass

    def rm_nao_determinismo(self) -> "Automato":
        """Remove não-determinismos do automato."""
        # TODO
        pass

    def rm_estados_inuteis(self) -> "Automato":
        """Remove estados inúteis do automato."""
        # TODO
        pass


# Maquina de estados
class MaquinaEstados:
    """Classe que implementa uma máquina de estados finitos 
    determinística por composição da classe Automato.
    """
    
    funcao_transicao: dict[dict[str, str]]
    estado_inicial: str
    estados_finais: set[str]


    def __init__(self, automato: Automato):
        self.transicao = automato.transicoes
        self.estados_finais = automato.estados_finais
        self.estado_inical = automato.estado_inicial
        self.estado_atual = automato.estado_inicial
        self.cadeia_restante = None
        self.posicao_cursor = 0
        self.movimentos = list()
    
    def config_seguinte(self, simbolo):
        """Aplica a função de transição δ(p, σ) -> q."""
        if simbolo != "\0":
            self.estado_atual = self.transicao[self.estado_atual][simbolo]
            self.posicao_cursor += 1

    def gravar_movimento(self, cadeia: deque[str]):
        """Retorna o histórico de movimentos da máquina de estados."""
        self.movimentos.append((self.estado_atual, "".join(cadeia)))

    def apresentar_movimentos(self):
        """Formata o conteúdo do histórico de movimentos da máquina de 
        estados usando o símbolo da catraca.
        """
        mov_formatados = str(self.movimentos).replace("), ", ") ⊢ ")
        return mov_formatados

    def resetar(self):
        """Reseta a máquina de estados."""
        self.estado_atual = self.estado_inical
        self.cadeia_restante = None
        self.posicao_cursor = 0
        self.movimentos = list()

    # Opcao com recursao
    def reconhecer_cadeia(self, cadeia):
        """Reconhece uma cadeia na fita usando recursão."""

        if self.cadeia_restante == None:
            self.movimentos = []
            self.movimentos.append((self.estado_atual, cadeia))
        
        resultado = False
        if (self.estado_atual, cadeia[0]) in self.transicao.keys():
        
            self.estado_atual = self.transicao[(self.estado_atual, cadeia[0])]
            self.cadeia_restante = cadeia[1:]
            self.movimentos.append((self.estado_atual, self.cadeia_restante))
            if self.cadeia_restante == "":
                return True if self.estado_atual in self.estados_finais else False
            else:
                resultado = self.reconhecer_cadeia(self.cadeia_restante)
        else:            
            return False
        self.estado_atual = self.estado_inical
        self.cadeia_restante = None
        return resultado

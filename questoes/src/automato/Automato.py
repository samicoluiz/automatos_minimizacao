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

    estados: set[str]
    alfabeto: set[str]
    transicoes: dict[dict[str, str]]
    estado_inicial: str
    conj_estados_finais: set[str]
    fita: deque[str]

    def __init__(self, estados, alfabeto, transicoes,
        estado_inicial, conj_estados_finais):
        self.estados: set = estados
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
        Q: {{{','.join(self.estados)}}}
        Σ: {{{self.alfabeto}}}
        δ: {self.maquina_estados.transicao}
        q0: {self.estado_inicial}
        F: {self.estados_finais}\
        """

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

        if cadeia == "":
            return True if self.estado_atual in self.estados_finais else False

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

class Transdutores(Automato):
    def __init__(self, estados, alfabeto_entrada, alfabeto_saida, transicoes, transducoes, estado_inicial, conj_estados_finais):
        super().__init__(estados, alfabeto_entrada, transicoes, estado_inicial, conj_estados_finais)
        self.alfabeto_saida = alfabeto_saida
        self.transducoes = transducoes
        self._cadeia_saida = ""
        self.posicao_cursor = 0

    def reconhecer_cadeia(self, cadeia):
        """Reconhece uma cadeia na fita usando recursão."""
        if self.maquina_estados.cadeia_restante == None:
            self.movimentos = []
            self.movimentos.append((self.maquina_estados.estado_atual, ''.join(cadeia)))
            self.posicao_cursor = 0

            if self.transducoes[self.maquina_estados.estado_atual] == "Fq30clG%6pYf":
                self._cadeia_saida = str(self.posicao_cursor - 10)
            else:
                self._cadeia_saida = self.transducoes[self.maquina_estados.estado_atual]
        
        resultado = False
        if self.maquina_estados.transicao[(self.maquina_estados.estado_atual, cadeia[0])]:
            
            self.maquina_estados.estado_atual = self.maquina_estados.transicao[(self.maquina_estados.estado_atual, cadeia[0])]
            if self.transducoes[self.maquina_estados.estado_atual] == "Fq30clG%6pYf":
                self._cadeia_saida += str(self.posicao_cursor - 10) + " "
            else:
                self._cadeia_saida += self.transducoes[self.maquina_estados.estado_atual]
            
            self.posicao_cursor += 1
            self.maquina_estados.cadeia_restante = cadeia[1:]
            self.movimentos.append((self.maquina_estados.estado_atual, self.maquina_estados.cadeia_restante))
            if not len(self.maquina_estados.cadeia_restante):
                return self._cadeia_saida if self.maquina_estados.estado_atual in self.estados_finais else False
            else:
                resultado = self.reconhecer_cadeia(self.maquina_estados.cadeia_restante)
        else:            
            return False
        
        self.maquina_estados.estado_atual = self.maquina_estados.estado_inical
        self.maquina_estados.cadeia_restante = None
        return resultado

    def transduzir_cadeia(self, cadeia):
        """Transduz uma cadeia na fita usando recursão."""

        # Fim da leiura da cadeia
        if cadeia == "" or cadeia == tuple():
            cadeia_final = self._cadeia_saida
            # Reseta resetando variáveis da máquina de estados
            self._cadeia_saida = ""
            self.posicao_cursor = 0
            return cadeia_final if self.maquina_estados.estado_atual in self.estados_finais else False

        # Transição não definida
        if (self.maquina_estados.estado_atual, cadeia[0]) not in self.maquina_estados.transicao.keys():
            try:
                self.maquina_estados.transicao[(self.maquina_estados.estado_atual, cadeia[0])]
            except KeyError:
                # Reseta resetando variáveis da máquina de estados
                print("Transição não definida")
                self._cadeia_saida = ""
                self.posicao_cursor = 0
                return False
        
        # Fazendo a mudança de estado
        self.maquina_estados.estado_atual = self.maquina_estados.transicao[(self.maquina_estados.estado_atual, cadeia[0])]
        # Construindo cadeia de saída
        if self.transducoes[self.maquina_estados.estado_atual] == "Fq30clG%6pYf":
            self._cadeia_saida += str(self.posicao_cursor - 10) + " "
        else:
            self._cadeia_saida += self.transducoes[self.maquina_estados.estado_atual]
        # Modificando a posição do cursor
        self.posicao_cursor += 1

        # Retornando resultado da função
        return self.transduzir_cadeia(cadeia[1:])
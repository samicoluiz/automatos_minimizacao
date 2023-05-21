
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

    def __init__(self, estados, alfabeto, transicoes,
        estado_inicial, conj_estados_finais):
        self.estados: set = estados
        self.alfabeto: set = alfabeto
        self.transicoes = transicoes
        self.estado_inicial = estado_inicial
        self.estados_finais = conj_estados_finais
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


    def resetar(self):
        """Reseta a máquina de estados."""
        self.estado_atual = self.estado_inical
        self.cadeia_restante = None
        self.posicao_cursor = 0
        self.movimentos = list()

    # Opcao com recursao
    def reconhecer_cadeia(self, cadeia, movimentos=[]):
        """Reconhece uma cadeia na fita usando recursão."""
        
        movimentos.append((self.estado_atual, cadeia))

        # Fim da leiura da cadeia
        if cadeia == "":
            estado_final = self.estado_atual
            # Resetando variáveis da máquina de estados
            self.estado_atual = self.estado_inical
            # Resultado
            self.movimentos = movimentos
            return True if estado_final in self.estados_finais else False

        # Transição não definida
        if (self.estado_atual, cadeia[0]) not in self.transicao.keys():
            # Resetando variáveis da máquina de estados
            self.estado_atual = self.estado_inical
            # Resultado
            self.movimentos = movimentos
            return False

        # Fazendo a mudança de estado
        self.estado_atual = self.transicao[(self.estado_atual, cadeia[0])]

        # Retornando resultado da função
        return self.reconhecer_cadeia(cadeia[1:])


class Transdutores(Automato):
    def __init__(self, estados, alfabeto_entrada, alfabeto_saida, transicoes, transducoes, estado_inicial, conj_estados_finais):
        super().__init__(estados, alfabeto_entrada, transicoes, estado_inicial, conj_estados_finais)
        self.alfabeto_saida = alfabeto_saida
        self.transducoes = transducoes
        self._cadeia_saida = ""
        self.posicao_cursor = 0

    def transduzir_cadeia(self, cadeia):
        """Transduz uma cadeia na fita usando recursão."""

        # Fim da leiura da cadeia
        if cadeia == "" or cadeia == tuple():
            estado_final = self.maquina_estados.estado_atual
            cadeia_final = self._cadeia_saida
            # Reseta resetando variáveis da máquina de estados
            self._cadeia_saida = ""
            self.posicao_cursor = 0
            self.maquina_estados.estado_atual = self.maquina_estados.estado_inical
            return cadeia_final if estado_final in self.estados_finais else False

        # Transição não definida
        if (self.maquina_estados.estado_atual, cadeia[0]) not in self.maquina_estados.transicao.keys():
            try:
                self.maquina_estados.transicao[(self.maquina_estados.estado_atual, cadeia[0])]
            except KeyError:
                # Reseta resetando variáveis da máquina de estados
                print("Transição não definida")
                self._cadeia_saida = ""
                self.posicao_cursor = 0
                self.maquina_estados.estado_atual = self.maquina_estados.estado_inical
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

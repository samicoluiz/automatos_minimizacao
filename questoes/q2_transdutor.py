from questoes.src.automato import Automato
from collections import defaultdict

estados = set(["q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "q10", "q11", "q12", "q13"])

diacriticos = set(['é', 'í', 'á', 'ó', 'ú', 'õ', 'ã', 'â', 'ê', 'ô', 'ç', 'à'])
alfabeto_entrada = set(set([chr(i) for i in range(32,128)]).union(diacriticos).union(set(map(str.upper, diacriticos))))

alfabeto_saida = [str(i) for i in range(10)]
transducoes = {
    'q0': '',
    'q1': '',
    'q2': '',
    'q3': '',
    'q4': '',
    'q5': '',
    'q6': '',
    'q7': '',
    'q8': '',
    'q9': '',
    'q10': '',
    'q11': '',
    'q12': '',
    'q13': 'Fq30clG%6pYf',
}

funcao_de_transicao = defaultdict(lambda: "q1")
funcao_de_transicao.update((
    (('q0', 'C'), 'q3'),
    (('q1', ' '), 'q2'),
    (('q2', 'C'), 'q3'),
    (('q2', 'c'), 'q3'),
    (('q2', ' '), 'q2'),
    (('q3', 'o'), 'q4'),
    (('q3', ' '), 'q2'),
    (('q4', 'm'), 'q5'),
    (('q4', ' '), 'q2'),
    (('q5', 'p'), 'q6'),
    (('q5', ' '), 'q2'),
    (('q6', 'u'), 'q7'),
    (('q6', ' '), 'q2'),
    (('q7', 't'), 'q8'),
    (('q7', ' '), 'q2'),
    (('q8', 'a'), 'q9'),
    (('q8', ' '), 'q2'),
    (('q9', 'd'), 'q10'),
    (('q9', ' '), 'q2'),
    (('q10', 'o'), 'q11'),
    (('q10', ' '), 'q2'),
    (('q11', 'r'), 'q12'),
    (('q11', ' '), 'q2'),
    (('q12', ','), 'q13'),
    (('q12', '?'), 'q13'),
    (('q12', ';'), 'q13'),
    (('q12', '!'), 'q13'),
    (('q12', ' '), 'q13'),
    (('q12', '.'), 'q13'),
    (('q12', ':'), 'q13'),
    (('q13', 'c'), 'q3'),
    (('q13', 'C'), 'q3'),
    (('q13', ' '), 'q2'))
)

estado_inicial = 'q0'
estados_finais = set(["q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "q10", "q11", "q12", "q13"])

transdutor_computador = Automato.Transdutores(estados, alfabeto_entrada, alfabeto_saida, funcao_de_transicao, transducoes, estado_inicial, estados_finais)

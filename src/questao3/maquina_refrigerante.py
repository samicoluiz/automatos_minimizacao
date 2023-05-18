from src.automato import Transdutores

# Automato de teste
estados = set(["q0", "q1", "q2", "q3"])
alfabeto_entrada = set(['0', '1', '2'])
alfabeto_saida = set(['1', '2'])
transducoes = {
    'q0': '1',
    'q1': '2',
    'q2': '1',
    'q3': '2',
}
funcao_de_transicao = {
    ('q0', '0'): 'q0',
    ('q0', '1'): 'q1',
    ('q0', '2'): 'q3',
    ('q1', '0'): 'q3',
    ('q1', '1'): 'q1',
    ('q1', '2'): 'q2',
    ('q2', '0'): 'q3',
    ('q2', '1'): 'q3',
    ('q2', '2'): 'q2',
    ('q3', '0'): 'q3',
    ('q3', '1'): 'q3',
    ('q3', '2'): 'q3',
}
estado_inicial = 'q0'
estados_finais = set(['q1', 'q2'])
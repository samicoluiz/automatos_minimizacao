from src.automato import Automato



estados = set(["q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "q10", "q11", "q12", "q13"])
diacriticos = set(['é', 'í', 'á', 'ó', 'ú', 'õ', 'ã', 'â', 'ê', 'ô', 'ç', 'à'])
alfabeto_entrada = set(set([chr(i) for i in range(32,128)]) + diacriticos + set(map(str.upper, diacriticos)))
print(alfabeto_entrada)


alfabeto_saida = [str(i) for i in range(10)]
transducoes = {
    'q0': '',
    'q1': '',
    'q2': '',
    'q3': '',
    'q4': '',
    'q5': '',
    'q6': '',
    '175': ''
}

funcao_de_transicao = {
    ('q0', 'C'): 'q3',
    ('q0', 1): 'q1',
    ('0', '100'): '100',
    ('25', '25'): '50',
    ('25', '50'): '75',
    ('25', '100'): '125',
    ('50', '25'): '75',
    ('50', '50'): '100',
    ('50', '100'): '150',
    ('100', '25'): '25',
    ('100', '50'): '50',
    ('100', '100'): '100',
    ('75', '25'): '100',
    ('75', '50'): '125',
    ('75', '100'): '175',
    ('125', '25'): '50',
    ('125', '50'): '75',
    ('125', '100'): '125',
    ('150', '25'): '75',
    ('150', '50'): '100',
    ('150', '100'): '150',
    ('175', '25'): '100',
    ('175', '50'): '125',
    ('175', '100'): '175'    
}



estado_inicial = '0'
estados_finais = set(["0", "25", "50", "75", "100", "125", "150", "175"])

#Instância
maquina_refri = Automato.Transdutores(estados, alfabeto_entrada, alfabeto_saida, funcao_de_transicao, transducoes, estado_inicial, estados_finais)
print(maquina_refri.reconhecer_cadeia(("50", "25", "50", "100", "25", "50", "100")))
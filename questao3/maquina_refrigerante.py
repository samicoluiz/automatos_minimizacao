# Automato de teste
from src.automato import Automato


estados = set(["0", "25", "50", "75", "100", "125", "150", "175"])
alfabeto_entrada = set(['25', '50', '100'])
alfabeto_saida = set(['0', '1'])
transducoes = {
    '0': '',
    '25': '0',
    '50': '0',
    '75': '0',
    '100': '1',
    '125': '1',
    '150': '1',
    '175': '1'
}
funcao_de_transicao = {
    ('0', '25'): '25',
    ('0', '50'): '50',
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
transdutor1 = Automato.Transdutores(estados, alfabeto_entrada, alfabeto_saida, funcao_de_transicao, transducoes, estado_inicial, estados_finais)

print(transdutor1.reconhecer_cadeia(("50", "25", "50", "100", "25", "50", "100")))
print("estou funcionando")
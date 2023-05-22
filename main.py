from questoes import q1_alpha, q1_beta, q1_charlie, q1_delta, q2_transdutor, q3_maquina_refrigerante
import os

cabecalho = """
        _________________________________________  
        ((                                     ))
        ))      TRABALHO SOBRE AUTOMATOS      (( 
        ((                                     ))
        -----------------------------------------  
"""

os.system("clear")
print(cabecalho)

print("""Questões disponíveis:

Nº - QUESTÃO
1  - Questão 1
2  - Questão 2
3  - Questão 3

(qualquer outra tecla + enter - encerrar o programa)
""")

n = input("Escolha uma questão para prosseguir.\nNº: ")

if n == "1":
    os.system("clear")
    print(cabecalho + "->QUESTÃO 1\n")
    alpha = q1_alpha.alpha
    beta = q1_beta.beta
    charlie = q1_charlie.charlie
    delta = q1_delta.delta

    questao1 = {
        "1": (alpha, "(ab*c*)*"),
        "2": (beta, "aaa(b|c)*|(b|c)*aaa)"),
        "3": (charlie, "a*b|ab*"),
        "4": (delta, "a*b*(a|ac*)")
    }

    print("Nº - LINGUAGENS")
    for numero, questao in questao1.items():
        print(f"{numero}  - Linguagem: {questao[1]}")
    q = input("\nEscolha uma linguagem para prosseguir.\nNº: ")

    if q in questao1.keys():
        escolha = questao1[q]
        os.system("clear")
        print(cabecalho + "->QUESTÃO 1\n" + "  ->LINGUAGEM: " + escolha[1] + "\n")

        print("AUTOMATO:\n", escolha[0])

        cadeia = input("\nInsira uma cadeia para validação no autômato: ")

        print("\nResultado:", "Aceita" if escolha[0].maquina_estados.reconhecer_cadeia(cadeia) else "Rejeitada")
        print("Movimentos: ", end="")
        for i in range(len(escolha[0].maquina_estados.movimentos)):
            if i == len(escolha[0].maquina_estados.movimentos) - 1:
                print(str(escolha[0].maquina_estados.movimentos[i]))
            else:
                print(str(escolha[0].maquina_estados.movimentos[i]), end=" ⊣ ")

        n = input("""
    OPÇÕES:
    1 - Validar outra cadeia
    2 - Escolher outra Linguagem
    3 - Voltar ao menu principal
    
    (qualquer outra tecla + enter - encerrar o programa)
    Nº: """)

elif n == "2":
    pass
elif n == "3":
    pass
else:
    print("Encerrando programa...")
    exit()
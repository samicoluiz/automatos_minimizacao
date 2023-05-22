from questoes import q1_alpha, q1_beta, q1_charlie, q1_delta, q2_transdutor, q3_maquina_refrigerante
import os

alpha = q1_alpha.alpha
beta = q1_beta.beta
charlie = q1_charlie.charlie
delta = q1_delta.delta
transdutor = q2_transdutor.transdutor_computador
maquina_refrigerante = q3_maquina_refrigerante.maquina_refri

cabecalho = """
        _________________________________________  
        ((                                     ))
        ))      TRABALHO SOBRE AUTOMATOS      (( 
        ((                                     ))
        -----------------------------------------  
"""

opcao = "3"
while opcao == "3":
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
        opcao = "2"
        while opcao == "2":
            os.system("clear")
            print(cabecalho + "->QUESTÃO 1\n")
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
                opcao = "1"
                while opcao == "1":
                    os.system("clear")
                    print(cabecalho + "->QUESTÃO 1\n" + "  ->LINGUAGEM: " + escolha[1] + "\n")

                    print("AUTOMATO:\n", escolha[0])

                    cadeia = input("\nInsira uma cadeia para validação no autômato: ")

                    print("\nResultado:", "Aceita" if escolha[0].maquina_estados.processar_cadeia(cadeia) else "Rejeitada")
                    print("Movimentos: ", end="")
                    for i in range(len(escolha[0].maquina_estados.movimentos)):
                        if i == len(escolha[0].maquina_estados.movimentos) - 1:
                            print(str(escolha[0].maquina_estados.movimentos[i]))
                        else:
                            print(str(escolha[0].maquina_estados.movimentos[i]), end=" ⊢ ")

                    opcao = input("""
                OPÇÕES:
                1 - Validar outra cadeia
                2 - Escolher outra Linguagem
                3 - Voltar ao menu principal
                
                (qualquer outra tecla + enter - encerrar o programa)
                Nº: """)

    elif n == "2":
        opcao = "2"
        while opcao == "2":
            os.system("clear")
            print(cabecalho + "->QUESTÃO 2\n")
            n = input("""Nº - OPÇÃO
1  - Validar com texto pronto
2  - Insirir texto para verificação

Nº: """)

            if n == "1":
                opcao = "1"
                while opcao == "1":
                    os.system("clear")
                    print(cabecalho + "->QUESTÃO 2\n" + """Texto:
                    O computador é uma máquina capaz de variados tipos de 
        tratamento automático de informações ou processamento de dados. 
        Entende-se por computador um sistema físico que realiza algum tipo 
        de computação. Assumiu-se que os computadores pessoais e laptops são 
        ícones da era da informação. O primeiro computador eletromecânico foi 
        construído por Konrad Zuse (1910–1995). Atualmente, um microcomputador 
        é também chamado computador pessoal ou ainda computador doméstico.
        """)

                    print("Posições que aparecem 'computador':", end=" ")
                    print(transdutor.processar_cadeia("""O computador é uma \
            máquina capaz de variados tipos de tratamento automático de informações \
            ou processamento de dados. Entende-se por computador um sistema físico \
            que realiza algum tipo de computação. Assumiu-se que os computadores \
            pessoais e laptops são ícones da era da informação. O primeiro \
            computador eletromecânico foi construído por Konrad Zuse (1910–1995). \
            Atualmente, um microcomputador é também chamado computador pessoal ou \
            ainda computador doméstico."""))

                    opcao = input("""Nº - OPÇÃO
                    1  - Validar com texto pronto
                    2  - Escolher outra opção
                    3  - Voltar ao menu principal
                    
                    (qualquer outra tecla + enter - encerrar o programa)
                    Nº: """)

            elif n == "2":
                opcao = "1"
                while opcao == "1":
                    os.system("clear")
                    print(cabecalho + "->QUESTÃO 2\n" + "  ->Insirir texto para verificação\n")

                    texto = input("Insira um texto para verificação: ")

                    print("Posições que aparecem 'computador':", end=" ")
                    print(transdutor.processar_cadeia(texto))

                    opcao = input("""Nº - OPÇÃO
                    1  - Verificar outra cadeia
                    2  - Escolher outra opção
                    3  - Voltar ao menu principal
                    
                    (qualquer outra tecla + enter - encerrar o programa)
                    Nº: """)


    elif n == "3":
        pass
    else:
        print("Encerrando programa...")
        exit()
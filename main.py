import questoes
import os

os.system("clear")
print("""
        _________________________________________  
        ((                                     ))
        ))      TRABALHO SOBRE AUTOMATOS      (( 
        ((                                     ))
        -----------------------------------------  
""")

print("""Questões disponíveis:

Nº - QUESTÃO
1  - Questão 1
2  - Questão 2
3  - Questão 3

(qualquer outra tecla + enter - encerrar o programa)
""")

n = input("Escolha uma questão para prosseguir.\nNº: ")

if n == "1":
    
    questoes.q1()
elif n == "2":
    questoes.q2()
elif n == "3":
    questoes.q3()
else:
    print("Encerrando programa...")
    exit()
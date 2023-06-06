from questoes import q2_transdutor

#Aceitacao
def test_validar_transdutor_computador_1() -> None:
    cadeia = "O computador é um conjunto de componentes eletrônicos capaz de executar variados tipos de algoritmos e tratamento de informações (processamento de dados)."
    esperado = "2 "
    assert q2_transdutor.transdutor_computador.processar_cadeia(cadeia) == esperado

def test_validar_transdutor_computador_2() -> None:
    cadeia = "Na loja de eletrônicos, encontrei um computador incrível. Decidi comprar o computador para substituir o antigo."
    esperado = "37 75 "
    assert q2_transdutor.transdutor_computador.processar_cadeia(cadeia) == esperado

def test_validar_transdutor_computador_3() -> None:
    cadeia = "Computador é uma máquina capaz de variados tipos de tratamento automático de informações ou processamento de dados."
    esperado = "0 "
    assert q2_transdutor.transdutor_computador.processar_cadeia(cadeia) == esperado

def test_validar_transdutor_computador_4() -> None:
    cadeia = "O computador é uma máquina capaz de variados tipos de tratamento automático de informações ou processamento de dados."
    esperado = "2 "
    assert q2_transdutor.transdutor_computador.processar_cadeia(cadeia) == esperado

def test_validar_transdutor_computador_5() -> None:
    cadeia = "Eu trabalho com computador durante o dia, à noite gosto de jogar jogos no meu computador e nos fins de semana utilizo o computador para aprender novas habilidades."
    esperado = "16 78 120 "
    assert q2_transdutor.transdutor_computador.processar_cadeia(cadeia) == esperado

#Rejeicao
def test_validar_transdutor_computador_6() -> None:
    cadeia = "Os computadores são ferramentas essenciais no mundo moderno, pois permitem a comunicação global, o acesso a informações instantâneas e a realização de tarefas complexas de maneira eficiente."
    esperado = "3 "
    assert q2_transdutor.transdutor_computador.processar_cadeia(cadeia) != esperado

def test_validar_transdutor_computador_7() -> None:
    cadeia = "O microcomputador, também conhecido como PC, é uma forma popular de computador pessoal. "
    esperado = "2 68 "
    assert q2_transdutor.transdutor_computador.processar_cadeia(cadeia) != esperado

def test_validar_transdutor_computador_8() -> None:
    cadeia = "A computadorização das empresas trouxe avanços significativos, automatizando processos, aumentando a eficiência e proporcionando um ambiente de trabalho mais produtivo."
    esperado = "2 "
    assert q2_transdutor.transdutor_computador.processar_cadeia(cadeia) != esperado
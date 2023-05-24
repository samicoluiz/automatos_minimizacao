from questoes import q2_transdutor

#Aceitacao
def test_validar_transdutor_computador_1() -> None:
    cadeia = "Era uma vez, um computador muito sabido que o Luiz Antônio comprou."
    esperado = "16 "
    assert q2_transdutor.transdutor_computador.processar_cadeia(cadeia) == esperado

def test_validar_transdutor_computador_2() -> None:
    cadeia = "Quando eu comprei um computador, eu fiquei muito feliz, pois ter um computador era meu sonho."
    esperado = "21 68 "
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
    cadeia = "Todos usamos computador."
    esperado = "13 "
    assert q2_transdutor.transdutor_computador.processar_cadeia(cadeia) == esperado

#Rejeicao
def test_validar_transdutor_computador_6() -> None:
    cadeia = "Os primeiros computadores eram grandes e pesados."
    esperado = "13 "
    assert q2_transdutor.transdutor_computador.processar_cadeia(cadeia) != esperado

def test_validar_transdutor_computador_7() -> None:
    cadeia = "Microcomputador é também chamado computador pessoal ou ainda computador doméstico."
    esperado = "5 33 61 "
    assert q2_transdutor.transdutor_computador.processar_cadeia(cadeia) != esperado

def test_validar_transdutor_computador_8() -> None:
    cadeia = "Todos somos computares, muahahah."
    esperado = "12 "
    assert q2_transdutor.transdutor_computador.processar_cadeia(cadeia) != esperado
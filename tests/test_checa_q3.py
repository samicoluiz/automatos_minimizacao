from questoes import q3_maquina_refrigerante

#Aceitacao
def test_validar_maquina_refri_1() -> None:
    cadeia = ("100", "50", "50")
    esperado = "101"
    assert q3_maquina_refrigerante.maquina_refri.processar_cadeia(cadeia) == esperado

def test_validar_maquina_refri_2() -> None:
    cadeia = ("100", "50", "50", "50", "50")
    esperado = "10101"
    assert q3_maquina_refrigerante.maquina_refri.processar_cadeia(cadeia) == esperado

def test_validar_maquina_refri_3() -> None:
    cadeia = ("100", "50", "50", "50", "50", "50", "50", "50", "50", "50")
    esperado = "1010101010"
    assert q3_maquina_refrigerante.maquina_refri.processar_cadeia(cadeia) == esperado

def test_validar_maquina_refri_4() -> None:
    cadeia = ("25", "100", "25", "50")
    esperado = "0101"
    assert q3_maquina_refrigerante.maquina_refri.processar_cadeia(cadeia) == esperado

#Rejeicao
def test_validar_maquina_refri_5() -> None:
    cadeia = ("100", "100", "50", "50")
    esperado = "1111"
    assert q3_maquina_refrigerante.maquina_refri.processar_cadeia(cadeia) != esperado

def test_validar_maquina_refri_6() -> None:
    cadeia = ("25", "25", "25", "25")
    esperado = "0010"
    assert q3_maquina_refrigerante.maquina_refri.processar_cadeia(cadeia) != esperado

def test_validar_maquina_refri_7() -> None:
    cadeia = ("25", "25", "50", "25")
    esperado = "0001"
    assert q3_maquina_refrigerante.maquina_refri.processar_cadeia(cadeia) != esperado
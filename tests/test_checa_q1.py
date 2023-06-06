from questoes import q1_alpha, q1_beta, q1_charlie, q1_delta

#### TESTES ALPHA ####
#Aceitacao


def test_validar_automato_alpha_1() -> None:
    cadeia = "aabbbcccab"
    assert q1_alpha.alpha.maquina_estados.processar_cadeia(cadeia)


def test_validar_automato_alpha_2() -> None:
    cadeia = "abbbaaabbbccccab"
    assert q1_alpha.alpha.maquina_estados.processar_cadeia(cadeia)


def test_validar_automato_alpha_3() -> None:
    cadeia = "acccccccab"
    assert q1_alpha.alpha.maquina_estados.processar_cadeia(cadeia)


def test_validar_automato_alpha_4() -> None:
    cadeia = "ab"
    assert q1_alpha.alpha.maquina_estados.processar_cadeia(cadeia)


def test_validar_automato_alpha_5() -> None:
    cadeia = "abbbbbbbbbbbbb"
    assert q1_alpha.alpha.maquina_estados.processar_cadeia(cadeia)


#Rejeicao
def test_validar_automato_alpha_6() -> None:
    cadeia = "bbaacc"
    assert q1_alpha.alpha.maquina_estados.processar_cadeia(cadeia) == 0


def test_validar_automato_alpha_7() -> None:
    cadeia = "abbbbacb"
    assert q1_alpha.alpha.maquina_estados.processar_cadeia(cadeia) == 0


def test_validar_automato_alpha_8() -> None:
    cadeia = "bbbbbbbbbbbbac"
    assert q1_alpha.alpha.maquina_estados.processar_cadeia(cadeia) == 0


def test_validar_automato_alpha_9() -> None:
    cadeia = "bcbc"
    assert q1_alpha.alpha.maquina_estados.processar_cadeia(cadeia) == 0


def test_validar_automato_alpha_10() -> None:
    cadeia = "cbcb"
    assert q1_alpha.alpha.maquina_estados.processar_cadeia(cadeia) == 0


#### TESTES BETA ####
#Aceitacao
def test_validar_automato_beta_1() -> None:
    cadeia = "aaa"
    assert q1_beta.beta.maquina_estados.processar_cadeia(cadeia)


def test_validar_automato_beta_2() -> None:
    cadeia = "aaabcbcccbccb"
    assert q1_beta.beta.maquina_estados.processar_cadeia(cadeia)


def test_validar_automato_beta_3() -> None:
    cadeia = "bbccbccbccbbcccbaaa"
    assert q1_beta.beta.maquina_estados.processar_cadeia(cadeia)


#Rejeicao
def test_validar_automato_beta_4() -> None:
    cadeia = "aaabccbbccaaa"
    assert q1_beta.beta.maquina_estados.processar_cadeia(cadeia) == 0


def test_validar_automato_beta_5() -> None:
    cadeia = "aaabcbcccbccba"
    assert q1_beta.beta.maquina_estados.processar_cadeia(cadeia) == 0


def test_validar_automato_beta_6() -> None:
    cadeia = "aaabcbccacbccb"
    assert q1_beta.beta.maquina_estados.processar_cadeia(cadeia) == 0


def test_validar_automato_beta_7() -> None:
    cadeia = "aabcbcccbccbc"
    assert q1_beta.beta.maquina_estados.processar_cadeia(cadeia) == 0


def test_validar_automato_beta_8() -> None:
    cadeia = "bcbcbcbbcb"
    assert q1_beta.beta.maquina_estados.processar_cadeia(cadeia) == 0


#### TESTES CHARLIE ####
#Aceitacao
def test_validar_automato_charlie_1() -> None:
    cadeia = "aaaaaab"
    assert q1_charlie.charlie.maquina_estados.processar_cadeia(cadeia)


def test_validar_automato_charlie_2() -> None:
    cadeia = "b"
    assert q1_charlie.charlie.maquina_estados.processar_cadeia(cadeia)


def test_validar_automato_charlie_3() -> None:
    cadeia = "abbbbbbbbb"
    assert q1_charlie.charlie.maquina_estados.processar_cadeia(cadeia)


def test_validar_automato_charlie_4() -> None:
    cadeia = "a"
    assert q1_charlie.charlie.maquina_estados.processar_cadeia(cadeia)


#Rejeicao
def test_validar_automato_charlie_5() -> None:
    cadeia = "bbaa"
    assert q1_charlie.charlie.maquina_estados.processar_cadeia(cadeia) == 0


def test_validar_automato_charlie_6() -> None:
    cadeia = "aabb"
    assert q1_charlie.charlie.maquina_estados.processar_cadeia(cadeia) == 0


def test_validar_automato_charlie_7() -> None:
    cadeia = "baaaaa"
    assert q1_charlie.charlie.maquina_estados.processar_cadeia(cadeia) == 0


def test_validar_automato_charlie_8() -> None:
    cadeia = "bbbbba"
    assert q1_charlie.charlie.maquina_estados.processar_cadeia(cadeia) == 0


#### TESTES DELTA ####
#Aceitacao
def test_validar_automato_delta_1() -> None:
    cadeia = "a"
    assert q1_delta.delta.maquina_estados.processar_cadeia(cadeia)


def test_validar_automato_delta_2() -> None:
    cadeia = "acccccc"
    assert q1_delta.delta.maquina_estados.processar_cadeia(cadeia)


def test_validar_automato_delta_3() -> None:
    cadeia = "aaaa"
    assert q1_delta.delta.maquina_estados.processar_cadeia(cadeia)


def test_validar_automato_delta_4() -> None:
    cadeia = "bbbaccc"
    assert q1_delta.delta.maquina_estados.processar_cadeia(cadeia)


def test_validar_automato_delta_5() -> None:
    cadeia = "aaaaccc"
    assert q1_delta.delta.maquina_estados.processar_cadeia(cadeia)


#Rejeicao
def test_validar_automato_delta_6() -> None:
    cadeia = "aaaabbbb"
    assert q1_delta.delta.maquina_estados.processar_cadeia(cadeia) == 0


def test_validar_automato_delta_7() -> None:
    cadeia = "bbbbaaab"
    assert q1_delta.delta.maquina_estados.processar_cadeia(cadeia) == 0


def test_validar_automato_delta_8() -> None:
    cadeia = "ccccaaba"
    assert q1_delta.delta.maquina_estados.processar_cadeia(cadeia) == 0


def test_validar_automato_delta_9() -> None:
    cadeia = "cccc"
    assert q1_delta.delta.maquina_estados.processar_cadeia(cadeia) == 0


def test_validar_automato_delta_10() -> None:
    cadeia = "bbbb"
    assert q1_delta.delta.maquina_estados.processar_cadeia(cadeia) == 0

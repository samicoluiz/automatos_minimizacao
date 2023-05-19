from src.automato import Automato

Q = {"q0", "q1", "q2", "q3", "q4"}
Alfabeto = {"a", "b"}
delta = {
    ('q0', 'a'): 'q1',
    ('q0', 'b'): 'q3',
    ('q1', 'a'): 'q2',
    ('q1', 'b'): 'q4',
    ('q2', 'a'): 'q2',
    ('q2', 'b'): 'q3',
    ('q4', 'b'): 'q4',
}
q0 = 'q0'
F = {"q1", "q3", "q4"}

charlie = Automato.Automato(Q, Alfabeto, delta, q0, F)

print(charlie.maquina_estados.reconhecer_cadeia("ba"), "não é aceito")
print(charlie.maquina_estados.reconhecer_cadeia("b"), "é aceito")

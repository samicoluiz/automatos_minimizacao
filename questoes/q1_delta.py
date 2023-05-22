from questoes.src.automato import Automato

Q = {"q0", "q1", "q2", "q3"}
Alfabeto = {"a", "b", "c"}
delta = {
    ('q0', 'a'): 'q1',
    ('q0', 'b'): 'q3',
    ('q1', 'c'): 'q2',
    ('q1', 'a'): 'q1',
    ('q1', 'b'): 'q3',
    ('q2', 'c'): 'q2',
    ('q3', 'b'): 'q3',
    ('q3', 'a'): 'q2',
}
q0 = 'q0'
F = {"q1", "q2"}

delta = Automato.Automato(Q, Alfabeto, delta, q0, F)


from src.automato import Automato

Q = {"q0", "q1", "q2", "q3"}
Alfabeto = {"a", "b", "c"}
delta = {
    ('q0', 'a'): 'q1',
    ('q0', 'b'): 'q3',
    ('q1', 'c'): 'q1',
    ('q1', 'a'): 'q2',
    ('q1', 'b'): 'q3',
    ('q2', 'a'): 'q2',
    ('q2', 'b'): 'q3',
    ('q2', 'c'): 'q1',
    ('q3', 'b'): 'q3',
    ('q3', 'a'): 'q1',
}
q0 = 'q0'
F = {"q1"}

delta = Automato.Automato(Q, Alfabeto, delta, q0, F)


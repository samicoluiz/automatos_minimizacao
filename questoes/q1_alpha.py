from src.automato import Automato

Q = {"q0", "q1", "q2"}
Alfabeto = {"a", "b", "c"}
delta = {
    ('q0', 'a'): 'q1',
    ('q1', 'a'): 'q1',
    ('q1', 'b'): 'q1',
    ('q1', 'c'): 'q2',
    ('q2', 'a'): 'q1',
    ('q2', 'c'): 'q2',
}
q0 = 'q0'
F = {"q0", "q1", "q2"}

alpha = Automato.Automato(Q, Alfabeto, delta, q0, F)

from src.automato import Automato

Q = {"q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7"}
Alfabeto = {"a", "b", "c"}
delta = {
    ('q0', 'a'): 'q1',
    ('q1', 'a'): 'q2',
    ('q2', 'a'): 'q3',
    ('q3', 'c'): 'q3',
    ('q3', 'b'): 'q3',
    ('q0', 'c'): 'q4',
    ('q0', 'b'): 'q4',
    ('q4', 'c'): 'q4',
    ('q4', 'b'): 'q4',
    ('q4', 'a'): 'q5',
    ('q5', 'a'): 'q6',
    ('q6', 'a'): 'q7',
}
q0 = 'q0'
F = {"q3", "q7"}

beta = Automato.Automato(Q, Alfabeto, delta, q0, F)



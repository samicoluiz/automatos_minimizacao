# Autômatos e Minimização

Implementação de autômatos finitos e transdutores para o trabalho da disciplina **Linguagens Formais, Autômatos e Computabilidade**.

## 📋 Sobre o Projeto

Este projeto implementa diferentes tipos de autômatos finitos determinísticos (AFD) e transdutores para demonstrar conceitos fundamentais da teoria da computação:

- **Questão 1**: Quatro autômatos finitos que reconhecem diferentes linguagens regulares
- **Questão 2**: Transdutor que identifica posições da palavra "computador" em textos
- **Questão 3**: Máquina de refrigerante que simula um sistema de vendas com moedas

## 🚀 Instalação e Execução

### Pré-requisitos

- Python 3.6 ou superior
- Sistema operacional compatível com Unix/Linux (para função `clear`)

### Executando o Projeto

1. Clone o repositório:
```bash
git clone https://github.com/samicoluiz/automatos_minimizacao.git
cd automatos_minimizacao
```

2. Execute o programa principal:
```bash
python3 main.py
```

3. Navegue pelo menu interativo para testar os diferentes autômatos.

## 🗂️ Estrutura do Projeto

```
automatos_minimizacao/
├── main.py                    # Interface principal do programa
├── questoes/                  # Implementações dos autômatos
│   ├── q1_alpha.py           # Autômato α: (ab*c*)*
│   ├── q1_beta.py            # Autômato β: aaa(b|c)*|(b|c)*aaa
│   ├── q1_charlie.py         # Autômato χ: a*b|ab*
│   ├── q1_delta.py           # Autômato δ: a*b*(a|ac*)
│   ├── q2_transdutor.py      # Transdutor para detectar "computador"
│   ├── q3_maquina_refrigerante.py # Máquina de refrigerante
│   └── src/
│       └── automato/
│           └── Automato.py   # Classes base para autômatos e transdutores
├── tests/                    # Testes unitários
│   ├── test_checa_q1.py     # Testes para os autômatos da questão 1
│   ├── test_checa_q2.py     # Testes para o transdutor
│   └── test_checa_q3.py     # Testes para a máquina de refrigerante
└── testes/                   # Notebooks experimentais
    └── notebook_experimentos.ipynb
```

## 📚 Questões Implementadas

### Questão 1: Autômatos Finitos Determinísticos

Implementação de quatro AFDs que reconhecem as seguintes linguagens regulares:

#### α (Alpha) - Linguagem: `(ab*c*)*`
- **Descrição**: Aceita cadeias formadas por repetições de sequências que começam com 'a', seguidas de zero ou mais 'b's e zero ou mais 'c's
- **Exemplos aceitos**: `"ab"`, `"abc"`, `"abbbccc"`, `"ababc"`
- **Exemplos rejeitados**: `"bac"`, `"cab"`, `"ba"`

#### β (Beta) - Linguagem: `aaa(b|c)*|(b|c)*aaa`
- **Descrição**: Aceita cadeias que começam com "aaa" seguido de qualquer combinação de 'b's e 'c's, OU qualquer combinação de 'b's e 'c's seguida de "aaa"
- **Exemplos aceitos**: `"aaa"`, `"aaabcbc"`, `"bcbcaaa"`
- **Exemplos rejeitados**: `"aa"`, `"aaabbbaaa"`, `"bcbc"`

#### χ (Charlie) - Linguagem: `a*b|ab*`
- **Descrição**: Aceita cadeias de zero ou mais 'a's seguidas de um 'b', OU um 'a' seguido de zero ou mais 'b's
- **Exemplos aceitos**: `"b"`, `"ab"`, `"aaab"`, `"abbb"`
- **Exemplos rejeitados**: `"ba"`, `"aabb"`, `"bbaa"`

#### δ (Delta) - Linguagem: `a*b*(a|ac*)`
- **Descrição**: Aceita cadeias de zero ou mais 'a's, seguidas de zero ou mais 'b's, terminando com 'a' ou 'a' seguido de zero ou mais 'c's
- **Exemplos aceitos**: `"a"`, `"bbbac"`, `"aaabbbaccc"`
- **Exemplos rejeitados**: `"bbbb"`, `"aaaabbbb"`, `"cccc"`

### Questão 2: Transdutor

Implementa um transdutor que processa texto em português e identifica todas as posições onde a palavra "computador" aparece.

#### Funcionalidades:
- Reconhece "computador" independente de maiúsculas/minúsculas
- Considera acentos e caracteres especiais do português
- Retorna as posições (índices) onde a palavra foi encontrada
- Trata pontuação adequadamente

#### Exemplo de uso:
```
Entrada: "O computador é útil. Meu computador é rápido."
Saída: "2 25 " (posições onde "computador" foi encontrado)
```

### Questão 3: Máquina de Refrigerante

Simula uma máquina de venda de refrigerantes que aceita moedas de 25, 50 e 100 centavos.

#### Funcionalidades:
- Estados representam o valor acumulado (0, 25, 50, 75, 100, 125, 150, 175)
- Refrigerante custa 100 centavos
- Dispensa refrigerante quando valor >= 100 centavos
- Fornece troco automaticamente
- Interface interativa para inserção de moedas

## 🧪 Executando os Testes

Para executar os testes (se pytest estiver instalado):
```bash
python3 -m pytest tests/ -v
```

Ou usando unittest do Python:
```bash
python3 -m unittest discover tests/ -v
```

## 💻 Interface do Usuário

O programa oferece uma interface de linha de comando intuitiva com menu de navegação:

```
        _________________________________________  
        ((                                     ))
        ))      TRABALHO SOBRE AUTOMATOS      (( 
        ((                                     ))
        -----------------------------------------  

Questões disponíveis:

Nº - QUESTÃO
1  - Questão 1
2  - Questão 2
3  - Questão 3

(qualquer outra tecla + enter - encerrar o programa)
```

### Navegação:
- **Questão 1**: Escolha entre os 4 autômatos e teste cadeias
- **Questão 2**: Valide textos pré-definidos ou insira seu próprio texto
- **Questão 3**: Simule a compra de refrigerante inserindo moedas

## 🏗️ Arquitetura

### Classes Principais:

#### `Automato`
Classe base que implementa um autômato finito determinístico seguindo a definição formal:
- **M = (Q, Σ, δ, q0, F)**
- Q: Conjunto finito de estados
- Σ: Alfabeto
- δ: Função de transição
- q0: Estado inicial
- F: Conjunto de estados finais

#### `MaquinaEstados`
Implementa a máquina de estados por composição, gerenciando:
- Estado atual
- Processamento de cadeias
- Histórico de movimentos
- Resetar estado

#### `Transdutores`
Extensão da classe `Automato` que implementa transdutores de estados finitos:
- Alfabeto de entrada e saída
- Função de transdução
- Processamento com geração de saída

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto é desenvolvido para fins acadêmicos como parte da disciplina de Linguagens Formais, Autômatos e Computabilidade.

## 👥 Autores

- **Sami Coluiz** - *Desenvolvimento inicial* - [samicoluiz](https://github.com/samicoluiz)

---

**Disciplina**: Linguagens Formais, Autômatos e Computabilidade  
**Universidade**: [Nome da Universidade]  
**Professor**: [Nome do Professor]

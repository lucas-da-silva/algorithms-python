<h1 align="center">Algoritmos</h1>

<p align="center">
    <img src="/.imgs/algorithms.png" width="100%" />
</p>

## Sobre o projeto

Foram implementados algoritmos de busca e ordenação, de maneira interativa e recursiva, analizando a complexidade de cada um.

## Tecnologias utilizadas

- [Python](https://www.python.org/) - Linguagem de programação interpretada de alto nível.
- [Pytest](https://docs.pytest.org/en/7.2.x/) - Framework de testes em Python.

## Funcionalidades dos algoritmos

#### [`study_schedule`](./challenges/challenge_study_schedule.py)

- Busca quantos estudantes estavam estudando em um determinado horário (`target_time`).

#### [`palindromes_recursive`](./challenges/challenge_palindromes_recursive.py)

- Verifica se uma string é um palíndromo de maneira recursiva.

#### [`anagrams`](./challenges/challenge_anagrams.py)

- Verifica se duas strings são anagramas uma da outra.

#### [`find_the_duplicate`](./challenges/challenge_find_the_duplicate.py)

- Encontra o primeiro número duplicado em uma lista.

#### [`palindromes_iterative`](./challenges/challenge_palindromes_iterative.py)

- Verifica se uma string é um palíndromo de maneira iterativa.

Além disso, foram desenvolvidos testes para a função [`encrypt_message`](./tests/encrypt/test_encrypt.py).

## Instalação

```bash
# Clonar Projeto
$ git clone git@github.com:lucas-da-silva/algorithms-python.git

# Entrar no diretório
$ cd algorithms-python

# Criar ambiente virtul e ativá-lo
$ python3 -m venv .venv && source .venv/bin/activate

# Instalar dependências
$ python3 -m pip install -r dev-requirements.txt

# Executar algoritmos
$ python3 challenges/main.py

# Executar testes
$ python3 -m pytest
```

## Estrutura do projeto

```
$PROJECT_ROOT
|   # Algoritmos de busca e ordenação
├── challenges
|   # Testes
└── tests
    |  # Testes da função encrypt_message
    └── encrypt
```

## Autor

- [@lucas-da-silva](https://github.com/lucas-da-silva)

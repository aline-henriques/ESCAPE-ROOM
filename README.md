# 🚀 Escape Room Lógico

Jogo em terminal desenvolvido em Python, com foco no ensino de lógica proposicional de forma interativa, progressiva e gamificada.
Desenvolvido por **Aline de Albuquerque Henriques**.

---

## Sobre o projeto

O **Escape Room Lógico** simula uma nave interestelar capturada por um vírus lógico.
O jogador assume o papel de tripulante e precisa resolver desafios de lógica proposicional para recuperar o controle da nave.

O jogo contém **5 módulos temáticos**, cada um com um **banco de 8 perguntas**.
A cada partida, **3 perguntas são sorteadas aleatoriamente** de cada banco — garantindo que o jogo seja diferente toda vez que você jogar.

---

## Objetivo

* Ensinar lógica proposicional de forma prática
* Desenvolver raciocínio lógico
* Aplicar conceitos em um ambiente gamificado
* Praticar organização de projetos em Python

---

## Módulos do jogo

| Módulo | Tema                     | Conteúdo                          |
| ------ | ------------------------ | --------------------------------- |
| 1      | Conectivos Lógicos       | ∧, ∨, ¬                           |
| 2      | Tabela-Verdade           | Implicação (→)                    |
| 3      | Implicação Lógica        | Argumentação (Modus Ponens, etc.) |
| 4      | Equivalência Lógica      | Leis de De Morgan, contrapositiva |
| 5      | Tautologia e Contradição | Classificação de proposições      |

A cada partida, **3 perguntas distintas** são sorteadas de cada módulo via `random.sample()`.

---

## ⚙️ Tecnologias utilizadas

* Python 3.10+
* Biblioteca `sys` — efeito typewriter no terminal
* Biblioteca `time` — pausas e animações
* Biblioteca `threading` — timer em thread paralela
* Biblioteca `random` — sorteio do banco de perguntas

---

## 📁 Estrutura do projeto

```
escape_room_logico/
├── main.py                <- ponto de entrada
├── game.py                <- motor do jogo e orquestração dos módulos
├── config.py              <- configurações globais
├── utils/
│   ├── display.py         <- funções de interface e feedback
│   └── timer.py           <- contagem regressiva opcional
└── fases/
├── conectivos.py          <- Módulo 1 (banco de 8 perguntas)
├── tabela_verdade.py      <- Módulo 2 (banco de 8 perguntas)
├── implicacao.py          <- Módulo 3 (banco de 8 perguntas)
├── equivalencia.py        <- Módulo 4 (banco de 8 perguntas)
└── tautologia.py          <- Módulo 5 (banco de 8 perguntas)
```

---

## ▶️ Como executar

### Pré-requisitos

* Python 3.10 ou superior

### Passo a passo

```bash
cd escape_room_logico
python main.py
```

---

## Executar uma fase isolada

```bash
python -c "from fases.conectivos import fase1; fase1()"
```

---

## Como funciona o jogo?

1. **Teste de admissão** — antes de iniciar, o jogador traduz `P → Q` para linguagem natural
2. **Sorteio** — 3 perguntas aleatórias são sorteadas do banco de cada módulo
3. **Desafio** — cada pergunta apresenta um enunciado lógico com múltipla escolha
4. **Tentativas** — o jogador tem `MAX_TENTATIVAS` por desafio (configurável em `config.py`)
5. **Dica** — ao esgotar as tentativas, uma dica pedagógica é exibida
6. **Progresso** — o contador `X/15` é atualizado a cada desafio concluído
7. **Vitória** — todos os 5 módulos concluídos liberta a nave

---

## Conceitos abordados

* **Conectivos lógicos** — conjunção (∧), disjunção (∨) e negação (¬)
* **Tabela-verdade** — construção e interpretação, com ênfase na implicação
* **Implicação lógica** — Modus Ponens, Modus Tollens e falácias lógicas
* **Equivalência lógica** — lei da implicação, leis de De Morgan, contrapositiva
* **Tautologia, contradição e contingência** — classificação de proposições compostas

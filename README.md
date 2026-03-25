# 🚀 Escape Room Lógico

Jogo em terminal desenvolvido em Python, com foco no ensino de lógica proposicional de forma interativa, progressiva e gamificada.
Desenvolvido por **Aline de Albuquerque Henriques**.

---

## Sobre o projeto

O **Escape Room Lógico** simula uma nave interestelar capturada por um vírus lógico.
O jogador assume o papel de tripulante e precisa resolver desafios para recuperar o controle da nave.

O jogo contém **10 desafios**, organizados em **5 módulos temáticos**.

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

---

## ⚙️ Tecnologias utilizadas

* Python 3.10+
* Biblioteca `sys`
* Biblioteca `time`
* Biblioteca `threading`

---

## 📁 Estrutura do projeto

```
escape_room_logico/
├── main.py
├── game.py
├── config.py
├── utils/
│   ├── display.py
│   └── timer.py
└── fases/
    ├── conectivos.py
    ├── tabela_verdade.py
    ├── implicacao.py
    ├── equivalencia.py
    └── tautologia.py
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

* Cada fase apresenta um desafio lógico
* O jogador possui tentativas limitadas
* Feedback imediato é fornecido a cada erro
* Dicas são exibidas para auxiliar o aprendizado
* O progresso é linear entre módulos

---

## Conceitos abordados

* Conectivos lógicos
* Tabela-verdade
* Implicação lógica
* Equivalência lógica
* Tautologia, contradição e contingência

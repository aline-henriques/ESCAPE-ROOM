# 🚀 Escape Room Lógico 

Um jogo educacional em Python que transforma lógica proposicional em uma experiência imersiva estilo escape room espacial.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?logo=python">
  <img src="https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow">
  <img src="https://img.shields.io/badge/UI-CustomTkinter-purple">
  <img src="https://img.shields.io/badge/Áudio-Pygame-green">
</p>

---

## Sobre o Projeto

O **Escape Room Lógico** é um jogo educacional interativo desenvolvido em Python, com foco no ensino de **lógica proposicional de forma gamificada**.

O jogador assume o papel de um astronauta em uma estação orbital comprometida por um “vírus lógico”, e precisa resolver desafios para restaurar os sistemas da nave e conseguir sair dela.

---

## Conteúdos Abordados

* Conectivos lógicos (∧, ∨, ¬)
* Tabela-verdade
* Implicação lógica (Modus Ponens / Modus Tollens)
* Equivalência lógica (Leis de De Morgan, contrapositiva)
* Tautologia, contradição e contingência

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia    | Função                  |
| ------------- | ----------------------- |
| Python 3.11   | Lógica do jogo          |
| Tkinter       | Interface base          |
| CustomTkinter | Interface moderna       |
| Pygame        | Áudio e efeitos         |
| JSON          | Persistência de ranking |

---

## 🧩 Estrutura do Projeto

```bash
escape-room/
│
├── back-end/
│   ├── main.py              # Entrada do sistema
│   ├── game.py              # Controlador do jogo
│   ├── config.py            # Configurações globais
│   │
│   ├── fases/               # Módulos de lógica
│   │   ├── conectivos.py
│   │   ├── tabela_verdade.py
│   │   ├── implicacao.py
│   │   ├── equivalencia.py
│   │   └── tautologia.py
│   │
│   ├── utils/               # Utilitários do sistema
│   │   ├── display.py       # Interface gráfica
│   │   ├── audio.py         # Sons e música
│   │   ├── timer.py         # Controle interno
│   │   └── ranking.py       # Sistema de ranking
│   │
│   ├── assets/              # Recursos do jogo
│   │   ├── music.mp3
│   │   ├── level_up.wav
│   │   ├── acesso_negado.wav
│   │   └── porta_abrindo.wav
│   │
│   └── ranking.json         # Pontuações salvas
│
└── README.md
```

---

## Funcionalidades

* Sistema de fases e progressão
* Interface gráfica interativa
* Feedback sonoro (acerto/erro/eventos)
* Sistema de pontuação
* Sistema de vida/tentativas
* Ranking persistente

---

## ▶️ Como Executar

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/escape-room-logico.git

# Acesse o projeto
cd escape-room-logico/back-end

# Instale dependências
pip install pygame customtkinter rich

# Execute
python main.py
```

---

## Status do Projeto

> Projeto em fase inicial de desenvolvimento

Próximas melhorias:

* Interface gráfica mais avançada
* Novas animações e efeitos visuais
* Expansão de módulos e fases
* Melhorias na experiência do usuário (UX)

---

## Roadmap

* [ ] Novos módulos de lógica
* [ ] Sistema de dificuldade
* [ ] Interface ainda mais interativa
* [ ] Ranking online
* [ ] Versão web futuramente

---

## Contribuições

Contribuições são bem-vindas!

```bash
Fork → Clone → Commit → Push → Pull Request
```

---

## 👩‍💻 Autora

**Aline de Albuquerque Henriques**
🎓 Ciência da Computação
💡 Foco em desenvolvimento e projetos práticos

---

## ⭐ Apoie o projeto

Se você gostou, deixe uma ⭐ no repositório! :)

# 🚀 Escape Room Lógico v2.0

Jogo educativo desenvolvido integralmente em Python, com foco no ensino de conceitos de lógica proposicional de forma interativa, progressiva e gamificada[cite: 8, 14]. [cite_start]O projeto simula uma nave interestelar comprometida por um vírus lógico, onde o jogador assume o papel de tripulante para restaurar os sistemas[cite: 9, 15].

Desenvolvido por **Aline de Albuquerque Henriques** para a disciplina de Lógica para Computação (UNICAP)

---

## ✨ Implementações e Diferenciais (v2.0)

* **Imersão Sonora**: Integração com a biblioteca `Pygame` para gerenciamento de trilha sonora e efeitos sonoros (SFX) durante acertos, erros e navegação.
* **Persistência de Dados**: Utilização de banco de dados local para salvar o progresso da missão e permitir o carregamento de partidas.
* **Ranking de Pilotos**: Sistema de pontuação acumulada com exibição de um "Top 10" para estimular o valor de replay.
* **Banco de Perguntas Aleatório**: Cada módulo possui 8 questões cadastradas, das quais 3 são sorteadas via `random.sample()` a cada partida, garantindo uma experiência única a cada sessão.

---

## 📁 Estrutura do Projeto

O sistema segue uma arquitetura modular para garantir alta coesão e facilidade de manutenção[cite: 11, 22].

```text
escape_room_logico/
├── main.py                <- Ponto de entrada do sistema 
├── game.py                <- Motor principal e controle de fluxo 
├── config.py              <- Parâmetros globais e constantes 
├── database.db            <- Banco de dados (SQLite) para saves e ranking
├── utils/                 <- Módulos auxiliares de utilidade 
│   ├── display.py         <- Interface narrativa e efeito typewriter 
│   ├── audio.py           <- Gerenciador de som (SFX e Música)
│   ├── banco.py           <- Manipulação do banco de dados (Ranking)
│   └── timer.py           <- Cronômetro em thread paralela 
└── fases/                 <- Conteúdo temático e bancos de perguntas 
    ├── conectivos.py      <- Módulo 1: Conectivos Lógicos 
    ├── tabela_verdade.py  <- Módulo 2: Tabela-Verdade 
    ├── implicacao.py      <- Módulo 3: Implicação Lógica 
    ├── equivalencia.py    <- Módulo 4: Equivalência Lógica 
    └── tautologia.py      <- Módulo 5: Tautologia e Contradição 
```

---

## ⚙️ Tecnologias Utilizadas

* **Python 3.10+**: Linguagem base do sistema.
* **Rich**: Formatação avançada e cores para interface via terminal.
* **Pygame**: Motor para execução de áudio e efeitos sonoros.
* **SQLite3**: Persistência de dados local.
* **Threading**: Execução de timer em segundo plano.

---

## 🎮 Como Jogar

1.  **Teste de Admissão**: O jogador deve traduzir corretamente uma condicional para avançar
2.  **Desafios**: Resolva 3 questões por módulo temático
3.  **Mecânicas**:
    * **Tentativas**: Cada desafio possui um limite de `MAX_TENTATIVAS`
    * **Dicas**: Mensagens pedagógicas são exibidas em caso de erro
    * **Progresso**: Acompanhamento em tempo real (ex: 5/15 sistemas restaurados)
4.  **Vitória**: A conclusão do 5º módulo libera a nave para o piloto

---

## 🔮 Evoluções Futuras (Roadmap)

* **Interface TUI**: Implementação de molduras estáticas e layouts fixos para maior imersão visual.
* **Comandos CLI**: Criação de atalhos globais (como `HELP` ou `STATUS`) para auxílio dinâmico durante as perguntas.

---

## ▶️ Execução

Instale as dependências necessárias:
```bash
pip install pygame rich
```

Inicie o jogo:
```bash
python main.py
```
```
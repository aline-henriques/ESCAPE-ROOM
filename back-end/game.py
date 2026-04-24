from utils import display
from utils.audio import iniciar_musica, tocar_sfx
from fases import conectivos, tabela_verdade, implicacao, equivalencia, tautologia
import textwrap


class EscapeRoomControlador:
    def __init__(self):
        self.app = display.inicializar_interface_grafica()

        self.MODULOS = [
            {"nome": "Conectivos Lógicos", "modulo": conectivos},
            {"nome": "Tabela-Verdade", "modulo": tabela_verdade},
            {"nome": "Implicação Lógica", "modulo": implicacao},
            {"nome": "Equivalência Lógica", "modulo": equivalencia},
            {"nome": "Tautologia / Contradição", "modulo": tautologia},
        ]

        self.piloto = "ASTRONAUTA"
        self.pontuacao = 0
        self.modulo_idx = 0
        self.pergunta_idx = 0
        self.tentativas = 0
        self.max_tentativas = 3
        self.vida = 1.0
        self.perguntas_atuais = []

        self.resposta_admissao = "se eu estudar, então vou passar na prova do professor lucas"

        self.app.btn_a.configure(command=lambda: self.checar_resposta("A"))
        self.app.btn_b.configure(command=lambda: self.checar_resposta("B"))
        self.app.btn_c.configure(command=lambda: self.checar_resposta("C"))
        self.app.btn_d.configure(command=lambda: self.checar_resposta("D"))
        display.atualizar_piloto(self.piloto)

        iniciar_musica()

        self.tela_menu_principal()

    def _desabilitar_botoes(self):
        self.app.btn_a.configure(state="disabled")
        self.app.btn_b.configure(state="disabled")
        self.app.btn_c.configure(state="disabled")
        self.app.btn_d.configure(state="disabled")

    def tela_menu_principal(self):
        self.modulo_idx = 0
        self.pergunta_idx = 0
        self.tentativas = 0
        self.pontuacao = 0
        self.vida = 1.0

        display.atualizar_pontos(self.pontuacao)
        display.atualizar_progresso(self.vida)
        display.atualizar_tentativas(0, self.max_tentativas)
        display.mostrar_menu_principal(
            ao_iniciar=self.iniciar_jogo,
            titulo="ESCAPE ROOM",
            subtitulo="JOGO DE LÓGICA | PIXEL GALAXY",
            descricao=(
                "Nave de treinamento orbitando Saturno.\n"
                "Resolva desafios de logica para estabilizar os sistemas\n"
                "e libertar os setores da estacao orbital."
            ),
            texto_botao="INICIAR JOGO",
        )

    def iniciar_jogo(self):
        display.mostrar_tela_jogo()
        display.esconder_campo_texto()
        display.resetar_botoes()
        self._desabilitar_botoes()
        display.atualizar_status("BRIEFING DA MISSÃO")
        display.atualizar_substatus("Sincronizando nave com o protocolo de lógica.")
        display.atualizar_modulo("PRÓLOGO")
        display.escrever_na_tela(
            "ANO 2149\n\n"
            "Astronauta, piloto da cápsula X-17, recebeu uma missão de emergência:\n"
            "a estação orbital perdeu o controle das portas e só comandos lógicos\n"
            "podem reativar os setores.\n\n"
            "Cada módulo resolvido libera uma nova área da nave.\n"
            "Falhas repetidas drenam seus recursos.\n\n"
            "Sistema iniciando em 3... 2... 1..."
        )
        self.app.after(10000, self.tela_admissao)


    def tela_admissao(self):
        display.atualizar_status("FASE DE ADMISSÃO")
        display.atualizar_substatus("Traduza a implicação lógica para frase natural.")
        display.atualizar_modulo("ADMISSÃO")
        display.atualizar_tentativas(0, self.max_tentativas)
        display.resetar_botoes()

        display.escrever_na_tela(
            "🚀 TESTE DE ADMISSÃO\n\n"
            "Considere:\n\n"
            "P: Se eu estudar\n"
            "Q: vou passar na prova do professor Lucas\n\n"
            "P -> Q\n\n"
            "Traduza para uma frase completa."
        )

        display.mostrar_campo_texto()

        self.app.btn_a.configure(text="ENVIAR", command=self.checar_admissao, state="normal")
        self.app.btn_b.configure(text="LIMPAR", command=display.limpar_campo_texto, state="normal")
        self.app.btn_c.configure(state="disabled")
        self.app.btn_d.configure(state="disabled")

    def checar_admissao(self):
        resposta = " ".join(display.obter_texto_digitado().lower().strip().split())

        if resposta == self.resposta_admissao:
            tocar_sfx("acerto")
            self.pontuacao += 100

            display.atualizar_pontos(self.pontuacao)
            display.escrever_na_tela("✅ ACESSO LIBERADO!")
            display.atualizar_substatus("Acesso autorizado. Preparando decolagem...")

            display.esconder_campo_texto()
            display.animar_vitoria_modulo()

            self.app.after(1300, self.iniciar_modulo)

        else:
            tocar_sfx("erro")

            self.tentativas += 1
            self.vida -= 0.1

            display.atualizar_tentativas(self.tentativas)
            display.atualizar_progresso(self.vida)

            display.escrever_na_tela(
                "❌ ERRADO!\n\n"
                "Traduza novamente a proposição:\n\n"
                "P: se eu estudar\n"
                "Q: vou passar na prova do professor Lucas\n\n"
                "P -> Q\n\n"
                "Escreva a frase completa em português."
            )
            display.atualizar_substatus("Quase lá. Releia o significado de P -> Q.")

            display.limpar_campo_texto()


    def iniciar_modulo(self):
        self.tentativas = 0
        display.resetar_botoes()

        self.app.btn_a.configure(command=lambda: self.checar_resposta("A"), state="normal")
        self.app.btn_b.configure(command=lambda: self.checar_resposta("B"), state="normal")
        self.app.btn_c.configure(command=lambda: self.checar_resposta("C"), state="normal")
        self.app.btn_d.configure(command=lambda: self.checar_resposta("D"), state="normal")

        if self.modulo_idx < len(self.MODULOS):
            modulo = self.MODULOS[self.modulo_idx]

            display.atualizar_status(f"MÓDULO {self.modulo_idx + 1}")
            display.atualizar_substatus(f"Tema: {modulo['nome']}")
            display.atualizar_modulo(modulo["nome"], self.modulo_idx + 1, len(self.MODULOS))
            display.atualizar_tentativas(0)

            self.perguntas_atuais = modulo["modulo"].sortear(3)
            self.pergunta_idx = 0

            self.mostrar_pergunta()
        else:
            self.vitoria_final()

    def mostrar_pergunta(self):
        pergunta = self.perguntas_atuais[self.pergunta_idx]
        modulo = self.MODULOS[self.modulo_idx]
        display.resetar_botoes()
        display.atualizar_status(
            f"MÓDULO {self.modulo_idx + 1}  •  QUESTÃO {self.pergunta_idx + 1}/3"
        )
        display.atualizar_substatus(f"Tema: {modulo['nome']}")

        texto = (
            f"{pergunta['titulo']}\n\n"
            f"{' '.join(pergunta['narrativa'])}\n\n"
            f"{' '.join(pergunta['enunciado'])}"
        )

        display.escrever_na_tela(texto)

        self.app.btn_a.configure(text=self._formatar_opcao("A", pergunta["opcoes"].get("A", "-")))
        self.app.btn_b.configure(text=self._formatar_opcao("B", pergunta["opcoes"].get("B", "-")))
        self.app.btn_c.configure(text=self._formatar_opcao("C", pergunta["opcoes"].get("C", "-")))
        self.app.btn_d.configure(text=self._formatar_opcao("D", pergunta["opcoes"].get("D", "-")))

    def _formatar_opcao(self, letra, texto):
        conteudo = f"{letra}) {texto}"
        return textwrap.fill(conteudo, width=72, subsequent_indent="   ")

    def checar_resposta(self, escolha):
        pergunta = self.perguntas_atuais[self.pergunta_idx]
        display.sinalizar_resposta(escolha, pergunta["correta"])

        if escolha == pergunta["correta"]:
            tocar_sfx("acerto")

            self.pontuacao += 100
            display.atualizar_pontos(self.pontuacao)
            display.atualizar_substatus("Resposta correta. Sistemas estabilizados.")

            self.pergunta_idx += 1

            if self.pergunta_idx < len(self.perguntas_atuais):
                self.app.after(1000, self.mostrar_pergunta)
            else:
                self.passar_modulo()

        else:
            tocar_sfx("erro")

            self.tentativas += 1
            display.atualizar_tentativas(self.tentativas)
            display.atualizar_substatus("Resposta incorreta. Ajuste a rota.")

            if self.tentativas >= self.max_tentativas:
                display.escrever_na_tela("💀 MÓDULO REINICIADO")
                display.atualizar_substatus("Tentativas esgotadas. Reiniciando setor.")
                self.app.after(2000, self.iniciar_modulo)
            else:
                display.escrever_na_tela(
                    f"❌ ERRADO!\nTentativa {self.tentativas}/3"
                )
                self.app.after(1500, self.mostrar_pergunta)

    def passar_modulo(self):
        tocar_sfx("porta")
        display.animar_vitoria_modulo()
        display.atualizar_substatus("Setor concluído. Abrindo acesso ao próximo.")

        self.modulo_idx += 1
        self.app.after(1400, self.iniciar_modulo)

    def vitoria_final(self):
        display.animar_vitoria_final()
        display.atualizar_status("MISSÃO CONCLUÍDA")
        display.atualizar_substatus("Você dominou os módulos de lógica.")
        display.atualizar_modulo("MISSÃO FINAL")
        display.resetar_botoes()

        display.escrever_na_tela(
            f"🏆 VITÓRIA!\n\n"
            f"Pontos finais: {self.pontuacao}\n\n"
            f"Você concluiu a missão com sucesso!"
        )

def iniciar():
    controlador = EscapeRoomControlador()
    controlador.app.mainloop()

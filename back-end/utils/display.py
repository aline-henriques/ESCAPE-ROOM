import tkinter as tk
import random
import math
import customtkinter as ctk
import tkinter.font as tkfont

app_instancia = None

class InterfaceGalaxia(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Escape Room Lógico | Pixel Galaxy")
        self.geometry("1280x760")
        self.minsize(1180, 700)

        self.configure(fg_color="#070014")

        self.w = 1280
        self.h = 760
        self.estrelas = []
        self.partes_astronauta = {}
        self.pulso = 0
        self._reseta_botoes_job = None
        self._astro_base_y = None
        self._resize_job = None
        self._walking_speed = 16
        self._walking_frame_ms = 18
        self.em_cena_final = False
        self._job_cena_final = None
        self._job_transicao = None
        self._pulse_final = 0.0
        self.taca_glow = None
        self.menu_estrelas = []
        self.menu_planetas = []
        self.menu_job = None
        self.menu_mouse_x = 0.5
        self.menu_mouse_y = 0.5

        self._definir_fontes_pixel()
        self.cores = {
            "bg": "#070014",
            "hud": "#10022A",
            "painel": "#13002F",
            "painel_interno": "#0D0121",
            "ciano": "#7DF9FF",
            "rosa": "#FF8AF3",
            "amarelo": "#FFE066",
            "verde": "#78FF87",
            "texto": "#FFFFFF",
            "erro": "#FF5C8A",
            "botao": "#1B0B45",
            "botao_hover": "#3A1B8F",
        }

        self.criar_layout()
        self.criar_tela_menu()
        self.ocultar_tela_jogo()
        self.bind("<Configure>", self._ao_redimensionar)
        self.after(100, self.criar_cenario)
        self.animar_tudo()

    def _definir_fontes_pixel(self):
        fontes = set(tkfont.families(self))
        candidatas = [
            "Minecraft",
            "Press Start 2P",
            "Pixeled",
            "Pixel Emulator",
            "Fixedsys",
            "Terminal",
            "Consolas",
        ]
        base = next((nome for nome in candidatas if nome in fontes), "Consolas")
        self.fonte_pixel = (base, 14, "bold")
        self.fonte_pixel_titulo = (base, 20, "bold")
        self.fonte_pixel_texto = (base, 15)
        self.fonte_opcao = (base, 12, "bold")

    def criar_layout(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.canvas = tk.Canvas(self, bg=self.cores["bg"], highlightthickness=0)
        self.canvas.grid(row=0, column=0, sticky="nsew")

        self.hud = ctk.CTkFrame(
            self,
            fg_color=self.cores["hud"],
            border_width=2,
            border_color=self.cores["ciano"],
            corner_radius=8,
        )
        self.hud.place(relx=0.03, rely=0.022, relwidth=0.94, relheight=0.102)

        self.hud.grid_columnconfigure(0, weight=3)
        self.hud.grid_columnconfigure(1, weight=2)
        self.hud.grid_columnconfigure(2, weight=3)
        self.hud.grid_rowconfigure((0, 1), weight=1)

        self.lbl_piloto = ctk.CTkLabel(
            self.hud, text="PILOTO: ALINE", font=self.fonte_pixel, text_color=self.cores["ciano"]
        )
        self.lbl_piloto.grid(row=0, column=0, sticky="w", padx=(18, 8), pady=(8, 0))

        self.lbl_modulo = ctk.CTkLabel(
            self.hud,
            text="MODO: ADMISSÃO",
            font=(self.fonte_pixel[0], 11, "bold"),
            text_color=self.cores["rosa"],
        )
        self.lbl_modulo.grid(row=1, column=0, sticky="w", padx=(18, 8), pady=(0, 8))

        self.lbl_tentativas = ctk.CTkLabel(
            self.hud,
            text="TENTATIVAS: 0/3",
            font=self.fonte_pixel,
            text_color=self.cores["rosa"],
        )
        self.lbl_tentativas.grid(row=0, column=1, sticky="w", padx=8, pady=(8, 0))

        self.lbl_score = ctk.CTkLabel(
            self.hud,
            text="PONTOS: 0",
            font=self.fonte_pixel,
            text_color=self.cores["amarelo"],
        )
        self.lbl_score.grid(row=1, column=1, sticky="w", padx=8, pady=(0, 8))

        self.lbl_vida = ctk.CTkLabel(
            self.hud, text="VIDA: 100%", font=self.fonte_pixel, text_color=self.cores["verde"]
        )
        self.lbl_vida.grid(row=0, column=2, sticky="e", padx=(8, 18), pady=(8, 0))

        self.vida_bar = ctk.CTkProgressBar(
            self.hud,
            width=250,
            height=14,
            progress_color=self.cores["verde"],
            fg_color="#2A145A",
            corner_radius=4,
        )
        self.vida_bar.set(1)
        self.vida_bar.grid(row=1, column=2, sticky="e", padx=(8, 18), pady=(0, 8))

        self.painel = ctk.CTkFrame(
            self,
            fg_color=self.cores["painel"],
            border_width=3,
            border_color=self.cores["ciano"],
            corner_radius=8,
        )
        self.painel.place(relx=0.055, rely=0.51, relwidth=0.89, relheight=0.27)

        self.painel.grid_columnconfigure(0, weight=1)
        self.painel.grid_rowconfigure(2, weight=1)

        self.lbl_status = ctk.CTkLabel(
            self.painel,
            text="FASE DE ADMISSÃO",
            font=self.fonte_pixel_titulo,
            text_color=self.cores["amarelo"],
        )
        self.lbl_status.grid(row=0, column=0, sticky="w", padx=18, pady=(12, 0))

        self.lbl_substatus = ctk.CTkLabel(
            self.painel,
            text="Decodifique a lógica para avançar na nave.",
            font=(self.fonte_pixel[0], 11),
            text_color="#C3C0FF",
            anchor="w",
        )
        self.lbl_substatus.grid(row=1, column=0, sticky="w", padx=18, pady=(0, 2))

        self.textbox = ctk.CTkTextbox(
            self.painel,
            font=self.fonte_pixel_texto,
            fg_color=self.cores["painel_interno"],
            text_color=self.cores["texto"],
            border_width=1,
            border_color="#2A145A",
            corner_radius=6,
            wrap="word",
            activate_scrollbars=True,
        )
        self.textbox.grid(row=2, column=0, sticky="nsew", padx=16, pady=(2, 10))

        self.btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.btn_frame.place(relx=0.055, rely=0.80, relwidth=0.89, relheight=0.18)

        self.btn_frame.grid_columnconfigure(0, weight=1)
        self.btn_frame.grid_rowconfigure((0, 1, 2, 3), weight=1)

        self.btn_a = self.criar_botao("A", 0)
        self.btn_b = self.criar_botao("B", 1)
        self.btn_c = self.criar_botao("C", 2)
        self.btn_d = self.criar_botao("D", 3)
        self.botoes_resposta = {
            "A": self.btn_a,
            "B": self.btn_b,
            "C": self.btn_c,
            "D": self.btn_d,
        }
        self._aplicar_wrap_botoes()
        self.mostrar_tela_jogo()
        self.criar_overlay_transicao()

    def criar_overlay_transicao(self):
        self.overlay = ctk.CTkFrame(
            self,
            fg_color="#070014",
            border_width=0,
            corner_radius=0,
        )
        self.overlay_lbl = ctk.CTkLabel(
            self.overlay,
            text="",
            font=(self.fonte_pixel[0], 16, "bold"),
            text_color=self.cores["ciano"],
        )
        self.overlay_lbl.place(relx=0.5, rely=0.5, anchor="center")
        self.overlay.place_forget()

    def transicao_curta(self, mensagem="CARREGANDO...", duracao=260, ao_final=None):
        if self._job_transicao:
            self.after_cancel(self._job_transicao)
            self._job_transicao = None
        self.overlay_lbl.configure(text=mensagem)
        self.overlay.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.overlay.lift()

        def finalizar():
            self.overlay.place_forget()
            if ao_final:
                ao_final()

        self._job_transicao = self.after(duracao, finalizar)

    def criar_tela_menu(self):
        self.menu_frame = ctk.CTkFrame(
            self,
            fg_color="#050011",
            border_width=0,
            corner_radius=0,
        )
        self.menu_canvas = tk.Canvas(self.menu_frame, bg="#050011", highlightthickness=0)
        self.menu_canvas.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.menu_canvas.bind("<Motion>", self._menu_motion)
        self.menu_canvas.bind("<Leave>", self._menu_leave)

        self.menu_titulo_canvas = self.menu_canvas.create_text(
            0, 0,
            text="ESCAPE ROOM",
            fill=self.cores["amarelo"],
            font=(self.fonte_pixel[0], 64, "bold"),
            anchor="center",
            tags=("menu_text",),
        )
        self.menu_subtitulo_canvas = self.menu_canvas.create_text(
            0, 0,
            text="LOGICO | PIXEL GALAXY",
            fill=self.cores["ciano"],
            font=(self.fonte_pixel[0], 16, "bold"),
            anchor="center",
            tags=("menu_text",),
        )

        self.btn_menu_iniciar = ctk.CTkButton(
            self.menu_frame,
            text="INICIAR JOGO",
            font=(self.fonte_pixel[0], 14, "bold"),
            width=310,
            height=56,
            corner_radius=10,
            border_width=2,
            border_color=self.cores["ciano"],
            fg_color="#1A0B45",
            hover_color="#3A1B8F",
            text_color=self.cores["texto"],
        )
        self.btn_menu_iniciar.place(relx=0.5, rely=0.60, anchor="center")

    def _menu_motion(self, evento):
        largura = max(1, self.menu_canvas.winfo_width())
        altura = max(1, self.menu_canvas.winfo_height())
        self.menu_mouse_x = min(1, max(0, evento.x / largura))
        self.menu_mouse_y = min(1, max(0, evento.y / altura))

    def _menu_leave(self, _evento):
        self.menu_mouse_x = 0.5
        self.menu_mouse_y = 0.5

    def desenhar_fundo_menu(self):
        if not hasattr(self, "menu_canvas"):
            return
        self.menu_canvas.delete("bg")
        self.menu_estrelas.clear()
        self.menu_planetas.clear()

        largura = max(1280, self.menu_canvas.winfo_width())
        altura = max(760, self.menu_canvas.winfo_height())

        c1 = (2, 0, 10)     # topo
        c2 = (9, 2, 35)     # meio
        c3 = (19, 6, 56)    # base

        def cor_hex(c):
            return "#{:02x}{:02x}{:02x}".format(c[0], c[1], c[2])

        def mix(a, b, t):
            return (
                int(a[0] + (b[0] - a[0]) * t),
                int(a[1] + (b[1] - a[1]) * t),
                int(a[2] + (b[2] - a[2]) * t),
            )

        passo = 3
        for y in range(0, altura, passo):
            t = y / max(1, altura - 1)
            if t < 0.55:
                cor = mix(c1, c2, t / 0.55)
            else:
                cor = mix(c2, c3, (t - 0.55) / 0.45)
            self.menu_canvas.create_rectangle(
                0, y, largura, min(altura, y + passo),
                fill=cor_hex(cor), outline="", tags=("bg",)
            )

        nebulas = [
            (0.22, 0.26, 140, 48, "#1A0D45"),
            (0.50, 0.22, 180, 56, "#20135A"),
            (0.78, 0.26, 140, 48, "#1A0D45"),
        ]
        for rx, ry, nw, nh, nc in nebulas:
            nx = int(largura * rx)
            ny = int(altura * ry)
            self.menu_canvas.create_oval(nx - nw, ny - nh, nx + nw, ny + nh, fill=nc, outline="", tags=("bg",))

        for _ in range(240):
            x = random.randint(0, largura)
            y = random.randint(0, int(altura * 0.72))
            size = random.choice([1, 1, 2, 2, 3])
            cor = random.choice(["#FFFFFF", "#7DF9FF", "#FFE066", "#FF8AF3"])
            estrela_id = self.menu_canvas.create_rectangle(
                x, y, x + size, y + size, fill=cor, outline="", tags=("bg",)
            )
            self.menu_estrelas.append(
                {"id": estrela_id, "x": x, "y": y, "size": size, "speed": random.uniform(0.12, 0.52), "depth": random.uniform(0.4, 1.0), "cor": cor}
            )

        def planeta(cx, cy, r, cor_base, cor_sombra, cor_brilho, anel=False, depth=1.0):
            ids = []
            ids.append(self.menu_canvas.create_oval(cx - r - 8, cy - r - 8, cx + r + 8, cy + r + 8, fill="#100826", outline=""))
            ids.append(self.menu_canvas.create_oval(cx - r, cy - r, cx + r, cy + r, fill=cor_base, outline=""))
            ids.append(self.menu_canvas.create_oval(cx - r * 0.1, cy - r, cx + r, cy + r, fill=cor_sombra, outline=""))
            ids.append(self.menu_canvas.create_oval(cx - r * 0.65, cy - r * 0.7, cx + r * 0.35, cy - r * 0.05, fill=cor_brilho, outline=""))
            for _ in range(2):
                rx = random.uniform(-r * 0.35, r * 0.2)
                ry = random.uniform(-r * 0.2, r * 0.3)
                rr = random.uniform(r * 0.10, r * 0.17)
                ids.append(self.menu_canvas.create_oval(cx + rx - rr, cy + ry - rr, cx + rx + rr, cy + ry + rr, fill=cor_sombra, outline=""))
            if anel:
                ids.append(
                    self.menu_canvas.create_oval(
                        cx - r - 42, cy - 11, cx + r + 42, cy + 11,
                        outline="#E9D5FF", width=2
                    )
                )
                ids.append(
                    self.menu_canvas.create_oval(
                        cx - r - 34, cy - 6, cx + r + 34, cy + 6,
                        outline="#C084FC", width=1
                    )
                )

            self.menu_planetas.append(
                {"ids": ids, "ox": 0.0, "oy": 0.0, "depth": depth, "phase": random.uniform(0, 6.2)}
            )
            for item in ids:
                self.menu_canvas.addtag_withtag("bg", item)

        planeta(int(largura * 0.18), int(altura * 0.28), 48, "#7C3AED", "#5B21B6", "#A78BFA", anel=True, depth=1.3)
        planeta(int(largura * 0.82), int(altura * 0.28), 48, "#14B8A6", "#0F766E", "#5EEAD4", depth=1.3)
        planeta(int(largura * 0.50), int(altura * 0.17), 22, "#3B82F6", "#1D4ED8", "#93C5FD", depth=0.7)

        self.menu_canvas.coords(self.menu_titulo_canvas, largura * 0.5, altura * 0.35)
        self.menu_canvas.coords(self.menu_subtitulo_canvas, largura * 0.5, altura * 0.44)
        self.menu_canvas.tag_raise("menu_text")

    def iniciar_animacao_menu(self):
        self.parar_animacao_menu()
        self.desenhar_fundo_menu()
        self.animar_menu()

    def parar_animacao_menu(self):
        if self.menu_job:
            self.after_cancel(self.menu_job)
            self.menu_job = None

    def animar_menu(self):
        if not self.menu_frame.winfo_ismapped():
            self.menu_job = None
            return

        largura = max(1280, self.menu_canvas.winfo_width())
        amplitude_x = (self.menu_mouse_x - 0.5) * 26
        amplitude_y = (self.menu_mouse_y - 0.5) * 14
        self._pulse_final += 0.07

        for estrela in self.menu_estrelas:
            estrela["x"] -= estrela["speed"]
            if estrela["x"] < -8:
                estrela["x"] = largura + random.randint(4, 30)
                estrela["y"] = random.randint(0, int(self.menu_canvas.winfo_height() * 0.72))
            px = estrela["x"] + amplitude_x * estrela["depth"] * 0.25
            py = estrela["y"] + amplitude_y * estrela["depth"] * 0.22
            s = estrela["size"]
            self.menu_canvas.coords(estrela["id"], px, py, px + s, py + s)
            if random.random() < 0.015:
                cor = "#FFFFFF" if estrela["cor"] != "#FFFFFF" else random.choice(["#7DF9FF", "#FFE066", "#FF8AF3"])
                self.menu_canvas.itemconfig(estrela["id"], fill=cor)

        for planeta in self.menu_planetas:
            tx = amplitude_x * planeta["depth"] + math.sin(self._pulse_final + planeta["phase"]) * 1.2
            ty = amplitude_y * planeta["depth"] + math.cos(self._pulse_final + planeta["phase"]) * 1.0
            dx = tx - planeta["ox"]
            dy = ty - planeta["oy"]
            for item in planeta["ids"]:
                self.menu_canvas.move(item, dx, dy)
            planeta["ox"] = tx
            planeta["oy"] = ty

        brilho = "#FFE066" if int(self._pulse_final * 8) % 2 == 0 else "#FFF1A5"
        self.menu_canvas.itemconfig(self.menu_titulo_canvas, fill=brilho)
        self.menu_job = self.after(40, self.animar_menu)

    def mostrar_menu(
        self,
        ao_iniciar=None,
        titulo="ESCAPE ROOM",
        subtitulo="LOGICO | PIXEL GALAXY",
        descricao=None,
        texto_botao="INICIAR JOGO",
    ):
        self.ocultar_tela_jogo()
        self.menu_canvas.itemconfig(self.menu_titulo_canvas, text=titulo)
        self.menu_canvas.itemconfig(self.menu_subtitulo_canvas, text=subtitulo)
        self.btn_menu_iniciar.configure(text=texto_botao)
        if ao_iniciar:
            self.btn_menu_iniciar.configure(command=ao_iniciar)
        self.menu_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.menu_frame.lift()
        self.menu_canvas.tag_raise("menu_text")
        self.btn_menu_iniciar.lift()
        self.iniciar_animacao_menu()

    def ocultar_menu(self):
        if hasattr(self, "menu_frame"):
            self.parar_animacao_menu()
            self.menu_frame.place_forget()

    def mostrar_tela_jogo(self):
        self.em_cena_final = False
        if self._job_cena_final:
            self.after_cancel(self._job_cena_final)
            self._job_cena_final = None
        self.ocultar_menu()
        self.hud.place(relx=0.03, rely=0.022, relwidth=0.94, relheight=0.102)
        self.painel.place(relx=0.055, rely=0.51, relwidth=0.89, relheight=0.27)
        self.btn_frame.place(relx=0.055, rely=0.80, relwidth=0.89, relheight=0.18)

    def ocultar_tela_jogo(self):
        self.hud.place_forget()
        self.painel.place_forget()
        self.btn_frame.place_forget()
        if hasattr(self, "entrada_resposta"):
            self.entrada_resposta.grid_remove()

    def _ao_redimensionar(self, _evento):
        if self._resize_job:
            self.after_cancel(self._resize_job)
        self._resize_job = self.after(150, self._aplicar_layout_dinamico)

    def _aplicar_layout_dinamico(self):
        self._resize_job = None
        if hasattr(self, "lbl_modulo"):
            self.lbl_modulo.configure(wraplength=max(160, int(self.winfo_width() * 0.28)))
        if hasattr(self, "lbl_substatus"):
            self.lbl_substatus.configure(wraplength=max(320, int(self.winfo_width() * 0.8)))
        if self.menu_frame.winfo_ismapped():
            self.desenhar_fundo_menu()
        self._aplicar_wrap_botoes()
        if not self.em_cena_final:
            self.criar_cenario()

    def _aplicar_wrap_botoes(self):
        largura = max(260, int(self.winfo_width() * 0.84))
        for botao in self.botoes_resposta.values():
            botao.configure(width=largura)

    def criar_botao(self, texto, row):
        btn = ctk.CTkButton(
            self.btn_frame,
            text=texto,
            height=42,
            font=self.fonte_opcao,
            fg_color=self.cores["botao"],
            hover_color=self.cores["botao_hover"],
            text_color=self.cores["texto"],
            border_width=2,
            border_color=self.cores["rosa"],
            corner_radius=8,
            anchor="w",
        )
        btn.grid(row=row, column=0, padx=8, pady=5, sticky="nsew")
        return btn

    def resetar_estilo_botoes(self):
        if self._reseta_botoes_job:
            self.after_cancel(self._reseta_botoes_job)
            self._reseta_botoes_job = None

        for botao in self.botoes_resposta.values():
            botao.configure(
                fg_color=self.cores["botao"],
                hover_color=self.cores["botao_hover"],
                border_color=self.cores["rosa"],
                text_color=self.cores["texto"],
            )

    def feedback_resposta(self, escolha, correta):
        self.resetar_estilo_botoes()

        if correta in self.botoes_resposta:
            self.botoes_resposta[correta].configure(
                fg_color="#0F5132",
                hover_color="#146C43",
                border_color=self.cores["verde"],
            )

        if escolha != correta and escolha in self.botoes_resposta:
            self.botoes_resposta[escolha].configure(
                fg_color="#5C1027",
                hover_color="#7B1535",
                border_color=self.cores["erro"],
            )

        self._reseta_botoes_job = self.after(1300, self.resetar_estilo_botoes)

    def criar_cenario(self):
        self.canvas.delete("all")
        self.estrelas.clear()
        self.partes_astronauta.clear()

        self.w = max(self.canvas.winfo_width(), 1180)
        self.h = max(self.canvas.winfo_height(), 700)

        self.criar_fundo_pixel()
        self.criar_estrelas_pixel()
        self.criar_planetas_pixel()
        self.criar_chao_pixel()
        self.criar_nave_pixel()
        self.desenhar_astronauta_pixel()

    def criar_fundo_pixel(self):
        faixas = [
            "#070014", "#09001B", "#0C0025", "#110036",
            "#150044", "#190052", "#1A0B63", "#211072"
        ]

        altura = self.h / len(faixas)

        for i, cor in enumerate(faixas):
            self.canvas.create_rectangle(
                0, i * altura, self.w, (i + 1) * altura,
                fill=cor,
                outline=""
            )

        for _ in range(55):
            x = random.randint(int(self.w * 0.35), self.w)
            y = random.randint(70, int(self.h * 0.50))
            size = random.choice([12, 16, 20, 24, 28])
            cor = random.choice(["#2A0A70", "#36118B", "#1D2D8F", "#3A136D"])
            self.canvas.create_rectangle(x, y, x + size, y + size, fill=cor, outline="")

        for y in range(0, int(self.h), 4):
            self.canvas.create_line(0, y, self.w, y, fill="#09001A")

    def criar_estrelas_pixel(self):
        for _ in range(190):
            x = random.randint(0, self.w)
            y = random.randint(0, int(self.h * 0.56))
            size = random.choice([2, 2, 2, 3, 4])
            cor = random.choice(["#FFFFFF", "#7DF9FF", "#FFE066", "#FF8AF3"])
            estrela = self.canvas.create_rectangle(x, y, x + size, y + size, fill=cor, outline="")
            self.estrelas.append((estrela, random.uniform(0.3, 1.0), cor))

    def criar_planetas_pixel(self):
        px, py = 105, 185
        cores = ["#7C3AED", "#8B5CF6", "#A78BFA", "#4C1D95"]
        for i in range(7):
            for j in range(7):
                if (i - 3) ** 2 + (j - 3) ** 2 <= 10:
                    self.canvas.create_rectangle(
                        px + i * 12, py + j * 12,
                        px + i * 12 + 12, py + j * 12 + 12,
                        fill=random.choice(cores),
                        outline=""
                    )

        self.canvas.create_rectangle(px - 30, py + 36, px + 120, py + 44, fill="#FF8AF3", outline="")

        px2, py2 = self.w - 210, 155
        for i in range(6):
            for j in range(6):
                if (i - 2.5) ** 2 + (j - 2.5) ** 2 <= 8:
                    self.canvas.create_rectangle(
                        px2 + i * 13, py2 + j * 13,
                        px2 + i * 13 + 13, py2 + j * 13 + 13,
                        fill=random.choice(["#14B8A6", "#2DD4BF", "#0F766E"]),
                        outline=""
                    )

    def criar_chao_pixel(self):
        y = self.h * 0.51

        self.canvas.create_rectangle(0, y, self.w, self.h, fill="#160B2E", outline="")
        self.canvas.create_rectangle(0, y, self.w, y + 8, fill="#7DF9FF", outline="")
        self.canvas.create_rectangle(0, y + 8, self.w, y + 18, fill="#33215E", outline="")

        for x in range(0, int(self.w), 38):
            altura = random.choice([10, 14, 18, 22])
            self.canvas.create_rectangle(
                x,
                y + 22,
                x + 26,
                y + 22 + altura,
                fill=random.choice(["#241047", "#2E145C", "#1B0B36"]),
                outline=""
            )

    def criar_nave_pixel(self):
        self.nave_cx = self.w * 0.68
        self.nave_y = self.h * 0.32

        cx, y = self.nave_cx, self.nave_y
        s = 14

        self.canvas.create_rectangle(cx - 190, y + 160, cx + 190, y + 180, fill="#05000F", outline="")

        corpo = [
            (-12, 2, 12, 9, "#7DF9FF"),
            (-15, 3, 15, 8, "#7DF9FF"),
            (-18, 4, 18, 7, "#1B0B45"),
            (-20, 5, 20, 6, "#1B0B45"),
            (-17, 6, 17, 8, "#2A145A"),
            (-13, 8, 13, 10, "#3A1B8F"),
        ]

        for x1, y1, x2, y2, cor in corpo:
            self.canvas.create_rectangle(
                cx + x1 * s, y + y1 * s,
                cx + x2 * s, y + y2 * s,
                fill=cor,
                outline=""
            )

        self.canvas.create_rectangle(cx - 55, y + 38, cx + 55, y + 82, fill="#05000F", outline="")
        self.canvas.create_rectangle(cx - 42, y + 50, cx + 42, y + 70, fill="#7DF9FF", outline="")

        for lx in [-115, 105, 145]:
            self.canvas.create_rectangle(cx + lx, y + 105, cx + lx + 18, y + 123, fill="#FFE066", outline="")

        piso_y = self.h * 0.52
        porta_x1 = cx - 214
        porta_x2 = cx - 138
        porta_y2 = piso_y - 2
        porta_y1 = porta_y2 - 124

        self.porta_moldura = self.canvas.create_rectangle(
            porta_x1, porta_y1, porta_x2, porta_y2,
            fill="#06102C", outline="#7DF9FF", width=2
        )
        self.canvas.create_rectangle(
            porta_x1 + 4, porta_y1 + 4, porta_x2 - 4, porta_y2 - 4,
            fill="#0A1A45", outline="#1E3A8A", width=1
        )

        self.porta = self.canvas.create_rectangle(
            porta_x1 + 8, porta_y1 + 8, porta_x2 - 8, porta_y2 - 8,
            fill="#0EA5E9", outline="#BAE6FD", width=2
        )
        self.porta_interna = self.canvas.create_rectangle(
            porta_x1 + 24, porta_y1 + 22, porta_x2 - 24, porta_y2 - 20,
            fill="#030712", outline="#67E8F9", width=2
        )
        self.porta_luz = self.canvas.create_rectangle(
            porta_x1 + 18, porta_y1 + 14, porta_x2 - 18, porta_y1 + 20,
            fill="#A5F3FC", outline=""
        )
        self.porta_puxador = self.canvas.create_rectangle(
            porta_x2 - 18, porta_y1 + 48, porta_x2 - 13, porta_y1 + 82,
            fill="#E2E8F0", outline=""
        )

        self.canvas.create_text(
            cx + 25, y + 130,
            text="X-17",
            fill="#FFE066",
            font=("Courier New", 24, "bold")
        )

        self.partes_porta_animaveis = [
            self.porta,
            self.porta_interna,
            self.porta_luz,
            self.porta_puxador,
        ]
        self.porta_top_fechada = porta_y1 + 8
        self.porta_top_aberta = self.porta_top_fechada - 68

        self.porta_x = porta_x1 + 30

    def desenhar_astronauta_pixel(self):
        self.astro_x = self.w * 0.13
        self.astro_y = self.h * 0.52
        self._astro_base_y = self.astro_y
        x, y = self.astro_x, self.astro_y

        def rect(nome, x1, y1, x2, y2, cor):
            self.partes_astronauta[nome] = self.canvas.create_rectangle(
                x + x1, y + y1, x + x2, y + y2,
                fill=cor,
                outline=""
            )

        rect("sombra", -34, 4, 34, 12, "#05000F")
        rect("perna_e", -18, -42, -6, 0, "#D9F3FF")
        rect("perna_d", 6, -42, 18, 0, "#D9F3FF")
        rect("corpo", -28, -92, 28, -42, "#FFFFFF")
        rect("peito", -14, -78, 14, -56, "#13002F")
        rect("visor_luz", -8, -72, 8, -64, "#7DF9FF")
        rect("braco_e", -44, -86, -28, -48, "#D9F3FF")
        rect("braco_d", 28, -86, 44, -48, "#D9F3FF")
        rect("mochila", 28, -82, 45, -50, "#7C8AA8")

        rect("cap1", -28, -142, 28, -126, "#FFFFFF")
        rect("cap2", -38, -126, 38, -96, "#FFFFFF")
        rect("cap3", -28, -96, 28, -84, "#FFFFFF")
        rect("visor", -24, -122, 24, -100, "#070014")
        rect("visor_brilho", -18, -116, -4, -108, "#7DF9FF")

    def mover_astronauta(self, dx):
        self.astro_x += dx
        for parte in self.partes_astronauta.values():
            self.canvas.move(parte, dx, 0)

    def abrir_porta(self):
        coords = self.canvas.coords(self.porta)
        if coords and coords[1] > self.porta_top_aberta:
            for parte in self.partes_porta_animaveis:
                self.canvas.move(parte, 0, -12)
            self.after(16, self.abrir_porta)

    def fechar_porta(self):
        coords = self.canvas.coords(self.porta)
        if coords and coords[1] < self.porta_top_fechada:
            for parte in self.partes_porta_animaveis:
                self.canvas.move(parte, 0, 12)
            self.after(16, self.fechar_porta)

    def animar_entrada_na_nave(self):
        self.abrir_porta()
        self.after(550, self.caminhar_para_porta)

    def caminhar_para_porta(self):
        if self.astro_x < self.porta_x:
            self.mover_astronauta(self._walking_speed)
            self.after(self._walking_frame_ms, self.caminhar_para_porta)
        else:
            for parte in self.partes_astronauta.values():
                self.canvas.itemconfig(parte, state="hidden")
            self.fechar_porta()
            self.after(420, self.resetar_astronauta)

    def resetar_astronauta(self):
        alvo = self.w * 0.13
        dx = alvo - self.astro_x

        for parte in self.partes_astronauta.values():
            self.canvas.move(parte, dx, 0)
            self.canvas.itemconfig(parte, state="normal")

        self.astro_x = alvo

    def desenhar_taca_vencedor(self, x, y):
        cor_taca = "#FFE066"
        cor_brilho = "#FFF3A8"
        cor_base = "#8A6A00"

        self.taca_glow = None
        self.canvas.create_rectangle(x, y, x + 40, y + 12, fill=cor_taca, outline="")
        self.canvas.create_rectangle(x + 3, y + 12, x + 37, y + 38, fill=cor_taca, outline="")
        self.canvas.create_rectangle(x + 12, y + 38, x + 28, y + 60, fill=cor_taca, outline="")
        self.canvas.create_rectangle(x + 7, y + 60, x + 33, y + 71, fill=cor_base, outline="")
        self.canvas.create_rectangle(x + 10, y + 63, x + 30, y + 68, fill=cor_brilho, outline="")
        self.canvas.create_rectangle(x - 11, y + 16, x + 1, y + 30, fill=cor_taca, outline="")
        self.canvas.create_rectangle(x + 39, y + 16, x + 51, y + 30, fill=cor_taca, outline="")

    def desenhar_card_game_over(self):
        card_w = 780
        card_h = 250
        x1 = int((self.w - card_w) / 2)
        y1 = int(self.h * 0.13)
        x2 = x1 + card_w
        y2 = y1 + card_h

        self.canvas.create_rectangle(x1, y1, x2, y2, fill="#120028", outline="#7DF9FF", width=3)

        passo = 18
        for x in range(x1 + passo, x2, passo):
            self.canvas.create_line(x, y1, x, y2, fill="#1C0B3D")
        for y in range(y1 + passo, y2, passo):
            self.canvas.create_line(x1, y, x2, y, fill="#1C0B3D")

        self.canvas.create_text(
            (x1 + x2) / 2,
            y1 + 92,
            text="FIM DE JOGO",
            fill="#FFE066",
            font=(self.fonte_pixel[0], 58, "bold"),
        )
        self.canvas.create_text(
            (x1 + x2) / 2,
            y1 + 182,
            text="Parabéns, você conseguiu sair da nave!",
            fill="#7DF9FF",
            font=(self.fonte_pixel[0], 20, "bold"),
        )

    def desenhar_spotlight_final(self):
        topo_x = self.w * 0.22
        topo_y = self.h * 0.06
        base_y = self.h * 0.52
        self.canvas.create_polygon(
            topo_x - 42, topo_y,
            topo_x + 42, topo_y,
            topo_x + 180, base_y,
            topo_x - 180, base_y,
            fill="#0B1133",
            outline="",
        )
        self.canvas.create_oval(
            self.w * 0.10, self.h * 0.50, self.w * 0.36, self.h * 0.60,
            outline="#2DD4BF", width=2
        )

    def animar_cena_final(self):
        return

    def animar_vitoria_final(self):
        self.em_cena_final = True
        self.hud.place_forget()
        self.painel.place_forget()
        self.btn_frame.place_forget()
        if hasattr(self, "entrada_resposta"):
            self.entrada_resposta.grid_remove()
        self.criar_cenario()
        alvo_x_astro = self.w * 0.22
        self.mover_astronauta(alvo_x_astro - self.astro_x)
        for parte in self.partes_astronauta.values():
            self.canvas.itemconfig(parte, state="normal")
            self.canvas.tag_raise(parte)
        self.desenhar_taca_vencedor(self.astro_x + 34, self.astro_y - 100)
        self.desenhar_card_game_over()

    def animar_tudo(self):
        self.pulso += 0.1

        for estrela, velocidade, cor_base in self.estrelas:
            self.canvas.move(estrela, -velocidade, 0)
            coords = self.canvas.coords(estrela)
            if coords and coords[0] < -6:
                self.canvas.move(estrela, self.w + 20, 0)

            if int(self.pulso * 9 + velocidade * 10) % 11 == 0:
                cor_twinkle = cor_base if random.random() > 0.3 else "#FFFFFF"
                self.canvas.itemconfig(estrela, fill=cor_twinkle)

        if self.partes_astronauta and self._astro_base_y is not None:
            deslocamento = math.sin(self.pulso * 1.5) * 0.45
            alvo_y = self._astro_base_y + deslocamento
            dy = alvo_y - self.astro_y
            if abs(dy) > 0.05:
                self.astro_y = alvo_y
                for parte in self.partes_astronauta.values():
                    self.canvas.move(parte, 0, dy)

        self.after(45, self.animar_tudo)

    def mostrar_admissao(self):
        self.lbl_status.configure(text="FASE DE ADMISSÃO")
        self.lbl_substatus.configure(text="Interprete P -> Q para liberar acesso.")
        escrever_na_tela(
            "TESTE DE ADMISSÃO\n\n"
            "Interprete a proposição lógica:\n\n"
            "P: se eu estudar\n"
            "Q: vou passar na prova do professor Lucas\n\n"
            "P -> Q\n\n"
            "Digite a frase completa em português."
        )


def inicializar_interface_grafica():
    global app_instancia
    app_instancia = InterfaceGalaxia()
    return app_instancia


def escrever_na_tela(texto):
    if app_instancia:
        app_instancia.textbox.configure(state="normal")
        app_instancia.textbox.delete("0.0", "end")
        app_instancia.textbox.insert("0.0", texto)
        app_instancia.textbox.configure(state="disabled")


def mostrar_menu_principal(
    ao_iniciar=None,
    titulo="ESCAPE ROOM",
    subtitulo="JOGO DE LÓGICA | PIXEL GALAXY",
    descricao=None,
    texto_botao="INICIAR",
):
    if app_instancia:
        app_instancia.mostrar_menu(
            ao_iniciar=ao_iniciar,
            titulo=titulo,
            subtitulo=subtitulo,
            descricao=descricao,
            texto_botao=texto_botao,
        )


def mostrar_tela_jogo():
    if app_instancia:
        app_instancia.mostrar_tela_jogo()


def transicao_curta(mensagem="CARREGANDO...", duracao=260, ao_final=None):
    if app_instancia:
        app_instancia.transicao_curta(mensagem=mensagem, duracao=duracao, ao_final=ao_final)


def atualizar_status(texto):
    if app_instancia:
        app_instancia.lbl_status.configure(text=texto)


def atualizar_substatus(texto):
    if app_instancia and hasattr(app_instancia, "lbl_substatus"):
        app_instancia.lbl_substatus.configure(text=texto)


def atualizar_piloto(nome):
    if app_instancia:
        app_instancia.lbl_piloto.configure(text=f"PILOTO: {nome}")


def atualizar_modulo(nome, atual=None, total=None):
    if app_instancia and hasattr(app_instancia, "lbl_modulo"):
        if atual is not None and total is not None:
            app_instancia.lbl_modulo.configure(text=f"SETOR {atual}/{total}: {nome}")
        else:
            app_instancia.lbl_modulo.configure(text=f"MODO: {nome}")


def atualizar_progresso(valor):
    if app_instancia:
        progresso = max(0, min(1, valor))
        app_instancia.vida_bar.set(progresso)
        app_instancia.lbl_vida.configure(text=f"VIDA: {int(progresso * 100)}%")


def atualizar_pontos(pontos):
    if app_instancia:
        app_instancia.lbl_score.configure(text=f"PONTOS: {pontos}")


def atualizar_tentativas(tentativas, maximo=3):
    if app_instancia:
        app_instancia.lbl_tentativas.configure(text=f"TENTATIVAS: {tentativas}/{maximo}")


def animar_vitoria_modulo():
    if app_instancia:
        app_instancia.animar_entrada_na_nave()


def animar_vitoria_final():
    if app_instancia:
        app_instancia.animar_vitoria_final()


def mostrar_campo_texto():
    if app_instancia:
        if not hasattr(app_instancia, "entrada_resposta"):
            app_instancia.entrada_resposta = ctk.CTkEntry(
                app_instancia.painel,
                placeholder_text="Digite sua resposta...",
                font=app_instancia.fonte_pixel_texto,
                height=36,
                corner_radius=6,
                fg_color="#080017",
                border_color="#7DF9FF",
                text_color="#FFFFFF",
                border_width=2,
            )
            app_instancia.entrada_resposta.grid(
                row=3,
                column=0,
                sticky="ew",
                padx=16,
                pady=(0, 10),
            )
        else:
            app_instancia.entrada_resposta.grid(
                row=3,
                column=0,
                sticky="ew",
                padx=16,
                pady=(0, 10),
            )


def esconder_campo_texto():
    if app_instancia and hasattr(app_instancia, "entrada_resposta"):
        app_instancia.entrada_resposta.grid_remove()


def obter_texto_digitado():
    if app_instancia and hasattr(app_instancia, "entrada_resposta"):
        return app_instancia.entrada_resposta.get()
    return ""


def limpar_campo_texto():
    if app_instancia and hasattr(app_instancia, "entrada_resposta"):
        app_instancia.entrada_resposta.delete(0, "end")


def sinalizar_resposta(escolha, correta):
    if app_instancia:
        app_instancia.feedback_resposta(escolha, correta)


def resetar_botoes():
    if app_instancia:
        app_instancia.resetar_estilo_botoes()


def escrever(t, v=0):
    escrever_na_tela(t)


def imprimir_banner_assunto(n):
    atualizar_status(f"MÓDULO: {n.upper()}")


def imprimir_cabecalho(*a, **k): pass
def imprimir_separador(*a, **k): pass
def imprimir_sucesso(*a, **k): pass
def imprimir_falha(*a, **k): pass
def imprimir_fim_de_jogo(*a, **k): pass
def imprimir_vitoria(*a, **k): pass
def perguntar_multipla_escolha(*a, **k): return "A"

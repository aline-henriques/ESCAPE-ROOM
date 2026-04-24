# Contagem regressiva para o jogo

import threading
import time

class Timer:

    def __init__(self, segundos: int):
        self.segundos = segundos
        self.expirado = False
        self._rodando = False
        self._thread: threading.Thread | None = None

    def iniciar(self) -> None:
        self._rodando = True
        self.expirado = False
        self._thread = threading.Thread(target=self._executar, daemon=True)
        self._thread.start()

    def parar(self) -> None:
        self._rodando = False
        print("\r" + " " * 30 + "\r", end="", flush=True)

    def _executar(self) -> None:
        for restante in range(self.segundos, 0, -1):
            if not self._rodando:
                return
            print(f"\r  ⏱  Tempo restante: {restante:02d}s ", end="", flush=True)
            time.sleep(1)

        if self._rodando:
            self.expirado = True
            print("\r  ⏰  TEMPO ESGOTADO!                  ", flush=True)
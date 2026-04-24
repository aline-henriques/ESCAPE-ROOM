import os
import sys
from game import iniciar

if __name__ == "__main__":
    # Força os caminhos do Tcl/Tk para evitar erros de ambiente no Windows
    python_base = os.path.dirname(sys.executable)
    tcl_path = os.path.join(python_base, "tcl", "tcl8.6")
    tk_path = os.path.join(python_base, "tcl", "tk8.6")
    
    if os.path.exists(tcl_path):
        os.environ['TCL_LIBRARY'] = tcl_path
        os.environ['TK_LIBRARY'] = tk_path

    iniciar()
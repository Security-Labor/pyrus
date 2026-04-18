import sys
import os
# Certifique-se de que o arquivo anterior foi salvo como core.py
from core import executar

def show_help():
    print("""
Uso: python pyrus.py [comando] <argumentos>

Comandos disponíveis:
  run <arquivo.pyu>    Executa um script Pyrus.
  version              Exibe a versão atual do motor.
  help                 Mostra esta mensagem de ajuda.
    """)

def main():
    # Atualizado para v0.2.1 para alinhar com a nova lógica de If/Else
    BANNER = "🛡️ AEGIS Advanced Dynamics | Pyrus v0.2.1 Alpha"
    
    if len(sys.argv) < 2:
        print(BANNER)
        show_help()
        sys.exit(0)

    cmd = sys.argv[1]

    if cmd == "run":
        if len(sys.argv) < 3:
            print("❌ Erro: Especifique o caminho do arquivo .pyu")
            sys.exit(1)

        file_path = sys.argv[2]

        if not file_path.endswith('.pyu'):
            print("⚠️ Aviso: Arquivos Pyrus geralmente terminam em .pyu")

        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                codigo = f.read()
                # Chamando a nova função 'executar' do core.py
                executar(codigo)
        else:
            print(f"❌ Erro: O arquivo '{file_path}' não foi encontrado.")

    elif cmd == "version":
        print(BANNER)
        print("Build: 2026-04-17 | Stable Core: v0.2.1")

    elif cmd == "help":
        show_help()

    else:
        print(f"❓ Comando '{cmd}' desconhecido. Use 'python pyrus.py help'.")

if __name__ == "__main__":
    main()

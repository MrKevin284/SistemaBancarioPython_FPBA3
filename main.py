from banco import *
import interface

# Função principal para iniciar o sistema bancário
def main():
    # Inicializa o sistema bancário
    saldo = 1000  # Define um saldo inicial (pode ser personalizado)
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    # Inicializa a interface gráfica
    interface.inicializar_interface(saldo, limite, extrato, numero_saques, LIMITE_SAQUES)

if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import ttk
from funcoes import processar_escolha

# Função principal
def main():
    # Configurar a janela principal
    janela = tk.Tk()
    janela.title("RELATÓRIO CHATBOT")
    janela.geometry("350x100")
    janela.resizable(False, False)
    separador = ttk.Separator(janela, orient="horizontal")
    separador.pack(fill="x", pady=5)

    # Adicionar a mensagem inicial
    mensagem_inicial = tk.Label(janela, text="Olá, o Sr. deseja o relatório dos jogos de hoje?", font=("Helvetica", 10, "bold"))
    mensagem_inicial.pack(pady=10)

    # Adicionar botões SIM e NÃO
    botao_sim = tk.Button(janela, text="SIM", command=lambda: processar_escolha("SIM"))
    botao_sim.pack(side=tk.LEFT, padx=(120, 5))

    botao_nao = tk.Button(janela, text="NÃO", command=lambda: processar_escolha("NÃO"))
    botao_nao.pack(side=tk.RIGHT, padx=(5, 120))

    # Iniciar o loop principal da GUI
    janela.mainloop()

if __name__ == "__main__":
    main()

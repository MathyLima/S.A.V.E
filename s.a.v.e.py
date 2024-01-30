import json
from agente_secretaria import SecretariaGUI
from tkinter import Tk, filedialog

# Função para ler dados do arquivo config.json
def ler_configuracoes():
    try:
        with open("config.json", "r") as arquivo:
            dados = json.load(arquivo)
            return dados.get("logins", []), dados.get("senhas", [])
    except FileNotFoundError:
        print("Arquivo config.json não encontrado.")
        resposta = input("Deseja fornecer o caminho para um arquivo de configuração? (s/n): ").lower()
        if resposta == 's':
            return ler_arquivo_customizado()
        else:
            return [], []

# Função para ler dados de um arquivo fornecido pelo usuário
def ler_arquivo_customizado():
    root = Tk()
    root.withdraw()
    caminho_arquivo = filedialog.askopenfilename(title="Selecione um arquivo de configuração", filetypes=[("Arquivos JSON", "*.json")])
    root.destroy()

    if caminho_arquivo:
        try:
            with open(caminho_arquivo, "r") as arquivo:
                dados = json.load(arquivo)
                return dados.get("logins", []), dados.get("senhas", [])
        except FileNotFoundError:
            print(f"Arquivo {caminho_arquivo} não encontrado.")
    return [], []

# Exemplo de uso
lista_emails, lista_senhas = ler_configuracoes()
secretaria_gui = SecretariaGUI(lista_emails, lista_senhas)
secretaria_gui.run()

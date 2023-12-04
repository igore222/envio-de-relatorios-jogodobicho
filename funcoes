import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

    ##AQUI DAMOS PARTIDA A CONSTRUÇÃO DO TKINTER PARA A INTERFACE E INTEGRAÇÃO DA COLETA DOS DADOS JUNTAMENTE COM O ENVIO DO E-MAIL

    ##POP-UP (SIM)
def enviar_relatorio():
    mensagem = "Bons estudos."
    popup_janela = tk.Toplevel()
    popup_janela.title("Relatório Enviado")
    message_pop = tk.Label(popup_janela, text="E-mail enviado com sucesso!\n" + mensagem)
    message_pop.pack(padx=10, pady=10)
def nao_enviar_relatorio():
    popup_janela = tk.Toplevel()
    popup_janela.title("Aviso")
    mensagem_pop = tk.Label(popup_janela, text="Tudo bem, fico à disposição para servi-lo quando necessário.")
    mensagem_pop.pack(padx=10, pady=10)

# Função para lidar com a escolha do usuário (SIM ou NÃO)
def processar_escolha(escolha):
    if escolha == "SIM":
        enviar_relatorio()
    elif escolha == "NÃO":
        nao_enviar_relatorio()
    import requests
    from lxml import html
    import csv
    import os
    import smtplib
    from email.message import EmailMessage

    def extract_data(url):
        response = requests.get(url)

        if response.status_code == 200:

            tree = html.fromstring(response.content)

            # Elementos a serem extraidos pelo Xpath
            premios = [element.text_content().strip() for element in tree.xpath('//tr/td[1]')]
            resultados = [element.text_content().strip() for element in tree.xpath('//tr/td[2]')]
            bichos = [element.text_content().strip() for element in tree.xpath('//tr/td[3]')]

            # Criamos uma lista de dicionários
            data = [{'Prêmio': premio, 'Resultado': resultado, 'Bicho': bicho} for premio, resultado, bicho in
                    zip(premios, resultados, bichos)]

            # Pegamos os dados e importamos para o .csv
            with open('resultados.csv', 'w', newline='', encoding='utf-8') as csv_file:
                fieldnames = ['Prêmio', 'Resultado', 'Bicho']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

                # Escreve o cabeçalho
                writer.writeheader()

                # Escreve os dados
                writer.writerows(data)

            print("Dados exportados para 'resultados.csv'")

            return data  # Retorna os dados coletados

        else:
            print(f"Falha na solicitação. Código de status: {response.status_code}")
            return None

    # Site para coleta
    url = 'https://www.resultadosnahora.com.br/banca-lotep/'
    dados_coletados = extract_data(url)

    ## Envio da coleta dos dados por e-mail
    if dados_coletados:
        email = "e-mail de quem vai enviar"

        with open('senha.txt') as f:
            senha = f.readlines()
            f.close()

        senha_do_email = senha[0]

        msg = EmailMessage()
        msg['Subject'] = 'Resultados, dos jogos de hoje'
        msg['From'] = 'e-mail que vai enviar'
        msg['To'] = 'e-mail de quem vai receber'

        # Mensagem do corpo do e-mail usando os dados coletados
        corpo_email = "Segue o relatório diário:\n\n"
        msg.set_content(corpo_email)

        # Adicionamos o arquivo resultados.csv
        with open('resultados.csv', 'rb') as content_file:
            content = content_file.read()
            msg.add_attachment(content, maintype='application', subtype='csv', filename='resultados.csv')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email, senha_do_email)
            smtp.send_message(msg)

            print("E-mail enviado com sucesso!'")

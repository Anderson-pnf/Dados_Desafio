import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from bs4 import BeautifulSoup
import pandas as pd
import requests


html = 'https://bea3853.github.io/site_teste'

def obter_html(html):
    repostas = requests.get(html)
    return repostas.text

def extrair1():
    html_content = obter_html(html)
    soup = BeautifulSoup(html_content, 'html.parser')
    dados = soup.find('table')
    nome = []
    compra = []
    regiao = []
    
    linhas = dados.find_all('tr')[1:]
    for linha in linhas:
        n = linha.find_all('td')
        nome.append(n[0].text.strip())
        compra.append(int(n[1].text.strip()))
        regiao.append(n[2].text.strip())

    df = pd.DataFrame({'Nome': nome, 'Compra': compra, 'Regiao': regiao})

    contagem_nome = df['Nome'].value_counts()

    plt.plot(contagem_nome.index, contagem_nome.values)
    plt.xlabel('Nome')
    plt.ylabel('Compra')
    plt.title('Maior Comprador por Nome')
    plt.xticks(rotation=45)
    plt.show()

    estatistica = df.describe()
    text.config(text=text.cget("text") + "\n\n" + estatistica.to_string())

def extrair2():
    html_content = obter_html(html)
    soup = BeautifulSoup(html_content, 'html.parser')
    dados = soup.find('table')
    nome = []
    compra = []
    regiao = []

    linhas = dados.find_all('tr')[1:]
    for linha in linhas:
        n = linha.find_all('td')
        nome.append(n[0].text.strip())
        compra.append(int(n[1].text.strip()))
        regiao.append(n[2].text.strip())

    df = pd.DataFrame({'Nome': nome, 'Compra': compra, 'Regiao': regiao})

    soma_por_regiao = df.groupby('Regiao')['Compra'].sum()

    plt.bar(soma_por_regiao.index, soma_por_regiao.values)
    plt.xlabel('Região')
    plt.ylabel('Total de Compras')
    plt.title('Gráfico de Compras por Região')
    plt.xticks(rotation=45)
    plt.show()

    estatistica = df.describe()
    text.config(text=estatistica.to_string())

def extrair3():
    html_content = obter_html(html)
    soup = BeautifulSoup(html_content, 'html.parser')
    dados = soup.find('table')
    nome = []
    compra = []
    regiao = []

    linhas = dados.find_all('tr')[1:]
    for linha in linhas:
        n = linha.find_all('td')
        nome.append(n[0].text.strip())
        compra.append(int(n[1].text.strip()))
        regiao.append(n[2].text.strip())

    df = pd.DataFrame({'Nome': nome, 'Compra': compra, 'Regiao': regiao})

    soma_por_regiao = df.groupby('Nome')['Compra'].sum()

    plt.bar(soma_por_regiao.index, soma_por_regiao.values)
    plt.xlabel('Nome')
    plt.ylabel('Total de Compras')
    plt.title('Quantidade de Compras por Nome')
    plt.xticks(rotation=45)
    plt.show()

    estatistica = df.describe()
    text.config(text=estatistica.to_string())

janela = tk.Tk()

btn1 = tk.Button(janela, text = "Gráfico 1", command = extrair1)
btn1.pack()

btn2 = tk.Button(janela, text = "Gráfico 2", command = extrair2)
btn2.pack()

btn3 = tk.Button(janela, text = "Gráfico 3", command = extrair3)
btn3.pack()


janela.mainloop()
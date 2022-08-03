import tkinter as tk
from tkinter import ttk
import datetime as dt
import pandas as pd

#preciso criar um arquivo no excel pra poder fazer os teste de gravação deste
#programa

circuito = pd.read_excel('dados.xlsx', engine='openpyxl')

#criar uma lista
lista_privil = ['Ancião', 'Servo Ministerial', 'Pioneiro(a) regulares','Publicadores','Estudante']
lista_codigo = []


janela = tk.Tk()

#criar uma função
def inserir_codigo():
    descricao = entry_descricao.get()
    congreg = entry_congregacao.get()
    privilegio = combobox_privilegio.get()
    alvos = entry_AlvosEsp.get()
    data_criacao = dt.datetime.now()
    data_criacao = data_criacao.strftime('%d/%m/%Y - %H:%M')
    codigo = circuito.shape[0] + len(lista_codigo)+1
    codigo_str = f'COD-{codigo}'
    lista_codigo.append((codigo_str,descricao,privilegio,alvos,data_criacao))




# titulo da janela
janela.title('Cadastro de Publicações')

#--------------------------------------------------------------------------
#colocar texto dentro da janela
label_descricao = tk.Label(text='Nome do irmão: ')
label_descricao.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

#colocar um campo para o usuário escreva na janela
entry_descricao = tk.Entry()
entry_descricao.grid(row=2, column=0, padx=10, pady=10,sticky='nswe',columnspan=4)
#----------------------------------------------------------------------------

#--------------------------------------------------------------------------
#colocar_02 texto dentro da janela
label_congregacao = tk.Label(text='Qual congregação: ')
label_congregacao.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

#colocar um campo para o usuário escreva na janela
entry_congregacao = tk.Entry()
entry_congregacao.grid(row=4, column=0, padx=10, pady=10,sticky='nswe',columnspan=4)
#----------------------------------------------------------------------------

#--------------------------------------------------------------------------
#colocar um COMBOBOX dentro da janela
label_privilegio = tk.Label(text='Qual é o seu privilégio: ')
label_privilegio.grid(row=5, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

#colocar um COMBOBOX para o usuário escolher
combobox_privilegio = ttk.Combobox(values=lista_privil)
combobox_privilegio.grid(row=5, column=2,padx=10, pady=10, sticky='nswe', columnspan=2 )
#----------------------------------------------------------------------------


#colocar_03 texto dentro da janela
label_AlvosEsp = tk.Label(text='Qual é o seu alvos: ')
label_AlvosEsp.grid(row=6, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

#colocar um campo para o usuário escreva na janela
entry_AlvosEsp = tk.Entry()
entry_AlvosEsp.grid(row=6, column=2, padx=10, pady=10,sticky='nswe',columnspan=4)
#----------------------------------------------------------------------------


#criar um botão para criar um cadastro
botao_codigo = tk.Button(text='Criar Codigo', command=inserir_codigo)
botao_codigo.grid(row=7, column=0, padx=10, pady=10,sticky='nswe',columnspan=4)


janela.mainloop()

novo_circuito = pd.DataFrame(lista_codigo, columns=['CÓDIGO', 'DESCRIÇÃO', 'PRIVILÉGIO', 'ALVOS ESPIRITUAIS', 'DATA CRIAÇÃO'])
circuito = circuito.append(novo_circuito, ignore_index=True)
circuito.to_excel('dados.xlsx')


print(lista_codigo)



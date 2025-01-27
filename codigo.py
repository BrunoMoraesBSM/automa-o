
import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.5


# pyautogui.click -> clicar
# pyautogui.press -> pressionar uma tecla
# pyautogui.write -> escrever
# pyautogui.hotkey -> atalho de teclado (ctrl, C)

# Apertar a tecla window
pyautogui.press('win')

#Digitar chrome
pyautogui.write("Chrome")

# Apertar enter
pyautogui.press('enter')

# Escrever a URL do site
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

# pedir pro computador esperar 3 segundos
time.sleep(3)

# Passo 2: Fazer Login

# clicar no campo de email
pyautogui.click(x=2450, y=380)

# digitar o email
pyautogui.write('brunomoraes@outlook.com')

pyautogui.press('tab')
pyautogui.write('123456')

# Passar para o botão de login e clicar
pyautogui.press('tab')
pyautogui.press('enter')
# pyautogui.click(x=2609, y=541)

# Fechar a tela Chrome
time.sleep(0.5)
pyautogui.click(x=2780, y=371)

# MOLO000251,Logitech,Mouse,1,25.95,6.50,

# Passo 3: Importar a base de dados dos produtos

tabela = pd.read_csv('produtos.csv')
print(tabela)



# Passo 4: Cadastrar o produto

#clicar no primeiro espaçamento


for linha in tabela.index:
    pyautogui.click(x=2496, y=268)


    # codigo
    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(codigo)
    pyautogui.press('tab')

    # marca
    marca = tabela.loc[linha, 'marca']
    pyautogui.write(marca)
    pyautogui.press('tab')

    # tipo
    tipo = tabela.loc[linha, 'tipo']
    pyautogui.write(tipo)
    pyautogui.press('tab')

    # categoria
    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)
    pyautogui.press('tab')

    #preço_unitario
    preco_unitario = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preco_unitario)
    pyautogui.press('tab')

    #custo
    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write(custo)
    pyautogui.press('tab')

    #obs
    obs = str(tabela.loc[linha, 'obs'])
    if obs == 'nan':
        pyautogui.write('')
    else:
        pyautogui.write(obs)

    pyautogui.press('tab')

    # Enviar
    pyautogui.press('enter')
    pyautogui.press('enter')

    # numero positivo -> Scroll para cima
    # numero negativo -> para baixo

    pyautogui.scroll(1000)





'''
Paso 1: Abri o sistema da empresa
    sistema: https://dlp.hashtagtreinamentos.com/python/intensivao/login
Passo 2: Fazer o Login
Passo 3: Importar a base de dados dos produtos
Passo 4: Cadastrar 1 produto
Passo 5: Reperir o passo 4 até acabar todos os produtos
'''
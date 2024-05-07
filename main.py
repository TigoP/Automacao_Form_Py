############################ Passo a passo ############################
# instalar pyautogui: pip install pyautogui

import pyautogui
import time

pyautogui.PAUSE = 0.5 #usualmente para que um processo nao atropele o outro

#1 abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.press("enter")

pyautogui.click(x=779, y=607) #print(pyautogui.position())   ----> feito para pegar a posição do click (no meu caso, pois possuo duas contas no gmail)

#abrir o navegador (chrome na pagina desejada)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3) #caso a pagina demore a carregar, deixar um tempo de precaução

#2 fazer login
pyautogui.click(x=794, y=406) #print(pyautogui.position())
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab") #pula para o proximo campo do formulario
pyautogui.write("senha")
pyautogui.press("tab")
pyautogui.press("enter")

#3 importar a base de dados
#instalar pandas: pip install pandas numpy openpyxl
import pandas as pd #isto dá um apelido ao pandas. Ao invés de usar pandas.read ou pandas.xxx usa-se pd.read ou pd.alguma_coisa

tabela = pd.read_csv("produtos.csv") #peguei a base de dados e armazenei um uma variavel
print(tabela)

#4 cadastrar produto
for linha in tabela.index:
    #time.sleep(3)
    pyautogui.click(x=788, y=290) #print(pyautogui.position())
    pyautogui.hotkey("ctrl", "a")

    #aqui foi criado um caminho que recebe a  variavel tabela( contendo o arquivo csv) e LOCalizando a linha/titulo da coluna
    pyautogui.write(str(tabela.loc[linha, "codigo"])) 
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter")

    pyautogui.scroll(5000) # dica é scrollar um numero alto para ir até o topo da pagina

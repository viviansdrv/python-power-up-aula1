# https://www.youtube.com/watch?v=BxKahT39AGA
# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa
   # https://dlp.hashtagtreinamentos.com/python/intensivao/tabela
# Passo 2: Fazer login
# Passo 3: Importar a base de dados de produtos
# Passo 4: Cadastrar 1 produto
# Passo 5: Repetir o cadastro para todos os produtos

# pyautougui.click -> clicar com o mouse
# pyautogui.write -> escrever um texto
# pyautogui.press -> aperta 1 tecla
# pyautogui.hotkey -> atalho (combinação de teclas)
# pyautogui.hotkey("ctrl", "c")


# abrir o chrome
# entrar no link

# pyautogui.PAUSE = 0.3 faz uma pausa a cada comando. O time.sleep() a gente é quem define quando deve pausar
# esperar o site carregar
import pyautogui # pip install pyautogui
import time #p/ dar a pausa
import pandas as pd #pip install
#  pandas numpy openpyxlcodigo  

tabela = pd.read_csv("produtos.csv") #tem que estar no mesmo diretório

#pyautogui.PAUSE = 0.4
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.press("win")
time.sleep(2.5)
pyautogui.write("opera")
time.sleep(2.5)
pyautogui.press("enter")
time.sleep(8)
pyautogui.write(link)
time.sleep(2)
pyautogui.press("enter")  

time.sleep(3)
pyautogui.click(x=467, y=-695)
pyautogui.write("vivian@gmail.com")
time.sleep(2)
pyautogui.press("tab")
time.sleep(2)
pyautogui.write("senhaqualquer")
time.sleep(2)
pyautogui.press("enter")
time.sleep(2)

for linha in tabela.index:

   pyautogui.click(x=703, y=-807)
   time.sleep(1)

   codigo = tabela.loc[linha, "codigo"]
   marca = tabela.loc[linha, "marca"]
   # tipo = tabela.loc[linha, "tipo"] vou passar direto lá
   # categoria = tabela.loc[linha, "categoria"] vou passar direto lá
   # preco = tabela.loc[linha, "preco"]
   # custo = tabela.loc[linha, "custo"]

   pyautogui.write(str(codigo))
   time.sleep(0.5)
   pyautogui.press("tab")
   time.sleep(0.5)
   pyautogui.write(str(marca))
   time.sleep(0.5)
   pyautogui.press("tab")
   time.sleep(0.5)
   pyautogui.write(str(tabela.loc[linha, "tipo"]))
   time.sleep(0.5)
   pyautogui.press("tab")
   time.sleep(0.5)
   pyautogui.write(str(tabela.loc[linha, "categoria"]))
   time.sleep(0.5)
   pyautogui.press("tab")
   time.sleep(0.5)
   pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
   time.sleep(0.5)
   pyautogui.press("tab")
   time.sleep(0.5)
   pyautogui.write(str(tabela.loc[linha, "custo"]))
   time.sleep(0.5)
   pyautogui.press("tab")
   time.sleep(0.5)
   pyautogui.write(str(tabela.loc[linha, "custo"]))
   time.sleep(0.5)

   obs = tabela.loc[linha, "obs"]
   if not pd.isna(obs):
      pyautogui.write(str(tabela.loc[linha,"obs"]))

   pyautogui.press("tab")
   time.sleep(0.5)
   pyautogui.press("enter")
   time.sleep(0.7)
   pyautogui.scroll(50000)
311.0 


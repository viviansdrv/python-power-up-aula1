import pyautogui 
import time 
import pandas as pd


tabela = pd.read_csv("produtos.csv") 

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


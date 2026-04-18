from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from pynput.keyboard import Controller
import time

# Inicia o teclado e o navegador
teclado = Controller()
servico = Service()
opcoes = webdriver.ChromeOptions()
opcoes.add_argument("--start-maximized")
driver = webdriver.Chrome(service=servico, options=opcoes)

# Abre o Monkeytype
driver.get("https://monkeytype.com/")

# Espera a página carregar
time.sleep(5)

# Pressiona "Tab" e "Enter" para pular o tutorial
teclado.press('\t')
teclado.release('\t')
time.sleep(1)
teclado.press('\n')
teclado.release('\n')
time.sleep(2)

# Começa o loop para digitar
while True:
    try:
        palavras = driver.find_elements(By.CLASS_NAME, "word.active")
        for palavra in palavras:
            texto = palavra.text
            teclado.type(texto + " ")
            time.sleep(0.001)  # Espera mínima entre as palavras
    except Exception as e:
        print("Erro:", e)
        break

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

# Configura o navegador
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

# Abre o site Infinite Craft
driver.get("https://neal.fun/infinite-craft/")
time.sleep(5)

# Lista de elementos iniciais
descobertos = set()
novos = ['Water', 'Fire', 'Earth', 'Wind']

# Função para obter todos os elementos
def obter_elementos():
    cards = driver.find_elements(By.CLASS_NAME, "element")
    nomes = [c.text.strip() for c in cards if c.text.strip()]
    return cards, nomes

# Função para combinar elementos via JavaScript
def combinar(elem1, elem2):
    try:
        cards, nomes = obter_elementos()
        if elem1 not in nomes or elem2 not in nomes:
            return None

        # Localiza os elementos
        elem1_obj = next(c for c in cards if c.text.strip() == elem1)
        elem2_obj = next(c for c in cards if c.text.strip() == elem2)

        # Usa JavaScript para simular o drop
        js_code = """
        const dataTransfer = new DataTransfer();
        const dragStartEvent = new DragEvent('dragstart', { dataTransfer });
        const dropEvent = new DragEvent('drop', { dataTransfer });

        arguments[0].dispatchEvent(dragStartEvent);
        arguments[1].dispatchEvent(dropEvent);
        """
        driver.execute_script(js_code, elem1_obj, elem2_obj)
        time.sleep(1)

        # Verifica se apareceu novo elemento
        novos_cards, nomes_atuais = obter_elementos()
        for nome in nomes_atuais:
            if nome not in descobertos:
                print(f"🧪 Novo elemento: {nome}")
                novos.append(nome)
                descobertos.add(nome)
                break

        for nome in nomes_atuais:
            descobertos.add(nome)
    except Exception as e:
        print("Erro ao combinar:", e)

# Loop de combinações automáticas
try:
    while True:
        if len(novos) < 2:
            break
        e1 = random.choice(novos)
        e2 = random.choice(novos)
        print(f"Tentando: {e1} + {e2}")
        combinar(e1, e2)
        time.sleep(1)
except KeyboardInterrupt:
    print("Interrompido.")
finally:
    driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.firefox import GeckoDriverManager

import time
import random

# ==========================================
# CONFIG
# ==========================================

MAX_REMOVER = 300

# ==========================================
# FIREFOX
# ==========================================

driver = webdriver.Firefox(
    service=Service(GeckoDriverManager().install())
)

wait = WebDriverWait(driver, 20)

# ==========================================
# LOGIN
# ==========================================

driver.get("https://www.instagram.com/")

print("\nFaça login manualmente.\n")

input("Depois do login pressione ENTER...")

# ==========================================
# ABRIR SALVOS
# ==========================================

driver.get(
    "https://www.instagram.com/your_activity/saved/"
)

time.sleep(10)

removidos = 0

# ==========================================
# LOOP
# ==========================================

while removidos < MAX_REMOVER:

    try:

        # espera links aparecerem
        wait.until(
            EC.presence_of_all_elements_located(
                (By.TAG_NAME, "a")
            )
        )

        links = driver.find_elements(By.TAG_NAME, "a")

        post_url = None

        # debug
        print(f"\nLinks encontrados: {len(links)}")

        for link in links:

            href = link.get_attribute("href")

            if href:

                # DEBUG
                print(href)

                if (
                    "/p/" in href
                    or "/reel/" in href
                ):

                    post_url = href
                    break

        if not post_url:

            print("\nNenhum post encontrado.")

            # tenta scroll
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )

            time.sleep(5)

            continue

        print(f"\nAbrindo: {post_url}")

        driver.get(post_url)

        time.sleep(random.uniform(4, 6))

        # ==========================================
        # BOTÃO SALVO
        # ==========================================

        svgs = driver.find_elements(By.TAG_NAME, "svg")

        removeu = False

        for svg in svgs:

            aria = svg.get_attribute("aria-label")

            if aria:

                texto = aria.lower()

                if (
                    "saved" in texto
                    or "salv" in texto
                ):

                    try:

                        svg.click()

                        removidos += 1
                        removeu = True

                        print(
                            f"[+] Removido: {removidos}"
                        )

                        time.sleep(
                            random.uniform(3, 6)
                        )

                        break

                    except Exception as e:

                        print(e)

        if not removeu:

            print("Não conseguiu remover.")

        # volta
        driver.get(
            "https://www.instagram.com/your_activity/saved/"
        )

        time.sleep(random.uniform(5, 8))

    except Exception as e:

        print("\nERRO:")
        print(e)

        time.sleep(5)

# ==========================================
# FINAL
# ==========================================

print(f"\nFINALIZADO | {removidos} removidos")

driver.quit()

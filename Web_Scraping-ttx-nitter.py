from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
from datetime import datetime

USERNAME = "futebol_info"
URL = f"https://nitter.poast.org/{USERNAME}"

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(URL)

time.sleep(5)

posts = driver.find_elements(By.CSS_SELECTOR, "div.timeline-item")
print("Posts encontrados:", len(posts))

dados = []

def limpar_numero(valor):
    if not valor:
        return 0
    valor = valor.replace(",", "").replace(".", "").strip()
    return int(valor) if valor.isdigit() else 0

for post in posts:
    try:
        texto = post.find_element(By.CSS_SELECTOR, "div.tweet-content").text
        data_raw = post.find_element(By.CSS_SELECTOR, "span.tweet-date a").get_attribute("title")

        try:
            data_convertida = datetime.strptime(
                data_raw, "%b %d, %Y · %I:%M %p UTC"
            )
            data_formatada = data_convertida.strftime("%Y-%m-%d %H:%M:%S")
        except:
            data_formatada = data_raw

        stats = post.find_elements(By.CSS_SELECTOR, "div.tweet-stats span.tweet-stat")

        replies = limpar_numero(stats[0].text.strip()) if len(stats) > 0 else 0
        retweets = limpar_numero(stats[1].text.strip()) if len(stats) > 1 else 0
        likes = limpar_numero(stats[2].text.strip()) if len(stats) > 2 else 0
        views = limpar_numero(stats[3].text.strip()) if len(stats) > 3 else 0 

        dados.append({
            "autor": USERNAME,
            "texto": texto,
            "data_publicacao": data_formatada,
            "comentarios": replies,
            "reposts": retweets,
            "likes": likes,
            "visualizacoes": views
        })

    except Exception as e:
        print("erro ao processar post:", e)

driver.quit()

df = pd.DataFrame(dados)
df.to_csv("posts_nitterteste.csv", index=False, encoding="utf-8")

print("trquivo criado")
print("total coletado:", len(dados))
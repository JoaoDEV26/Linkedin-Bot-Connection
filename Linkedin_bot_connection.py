from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Abrir o LinkedIn
driver = webdriver.Chrome()
driver.get('https://br.linkedin.com/?trk=guest_homepage-basic_nav-header-logo')
sleep(2)

# Esperar e clicar no botão de login
wait = WebDriverWait(driver, 10)
botao_entrar = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='nav__button-secondary btn-md btn-secondary-emphasis']")))
botao_entrar.click()
sleep(3)
# Realizar o Login
email_lnkd = driver.find_element(By.ID, "username")
senha_lnkd = driver.find_element(By.ID, "password")
email_lnkd.send_keys('jgabriel261202@gmail.com ')
senha_lnkd.send_keys('Jgds2612.')

enviar_login = driver.find_element(By.XPATH, "//button[@aria-label='Entrar']")
enviar_login.click()
sleep(4)

# Pesquisar por categoria de trabalho
pesquisar = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Pesquisar']")))
pesquisar.send_keys("Desenvolvedor Python")
pesquisar.send_keys(Keys.ENTER)

# Filtrar pessoas
filtrar_pessoas = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Pessoas']")))
filtrar_pessoas.click()

while True:
    sleep(2)
    try:
        # Encontrar todos os botões "Conectar"
        conectar_pessoas = driver.find_elements(By.XPATH, "//button//span[text()='Conectar']")
        if not conectar_pessoas:
            print("Nenhum botão 'Conectar' encontrado.")
            break

        # Mandar mensagem para essas pessoas
        for botao in conectar_pessoas:
            sleep(3)
            botao.click()
            sleep(3)
            try:
                # Esperar pelo botão "Adicionar nota" e clicar
                botao_adicionar_nota = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Adicionar nota']")))
                driver.execute_script("arguments[0].click();", botao_adicionar_nota)
            except Exception as e:
                print(f"Erro ao clicar no botão 'Adicionar nota': {e}")
                continue

            sleep(1)
            mensagem = driver.find_element(By.XPATH,"//textarea[@id='custom-message']")
            mensagem.send_keys("Olá! Trabalho com Desenvolvimento Python e gostaria de manter conexão.")

            enviar_mensagem = driver.find_element(By.XPATH, "//button//span[text()='Enviar']")
            enviar_mensagem.click()
            sleep(3)
    except Exception as e:
        print(f"Erro: {e}")
        break

driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By

navegador = webdriver.Firefox()
navegador.get("https://class005.github.io/upaa-franciscomoratosp/adotecaes.html")
navegador.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div/a').click()
navegador.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/section/div/div/div/div[2]/div[1]/a/span').click()
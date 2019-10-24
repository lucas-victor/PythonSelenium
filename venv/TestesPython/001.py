'''

for item in novoUsuario:
    if 'cadastro' in novoUsuario:
        item.click()
    else:
        print('Elemento nao localizado.')
        print(item)

'''

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('C:\\Python\\chromedriver.exe')
driver.get('https://srbarriga.herokuapp.com/login')

#clica botao novo usuario
novoUsuario = driver.find_element_by_link_text('Novo usuário?')
novoUsuario.click()

nome = driver.find_element_by_name('nome')
nome.send_keys('lucas')

email = driver.find_element_by_name('email')
email.send_keys('teste@gmail.com')

senha = driver.find_element_by_name('senha')
senha.send_keys('123456')

btnCadastrar = driver.find_element_by_tag_name('input')
btnCadastrar.click()



time.sleep(2)
#driver.close()


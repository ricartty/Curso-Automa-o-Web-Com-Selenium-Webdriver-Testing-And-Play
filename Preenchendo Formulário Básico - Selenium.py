from selenium.webdriver import Chrome
from time import sleep

url = 'https://www.testingandplay.com/example/form'

navegador = Chrome()
navegador.get(url)

sleep (1)

email = navegador.find_element_by_xpath("//input[@name='email']")
email.click()
email.send_keys('ricarttymartins@gmail.com')

autocomplete = navegador.find_element_by_xpath("//input[@id='typeahead-basic']")
autocomplete.click()
autocomplete.send_keys('tex')
sleep (1)
span = autocomplete.find_element_by_xpath("//span[@class='mat-option-text']")
span.click()

select = navegador.find_element_by_xpath("//select[@id='select-input']")
select.click()
option = select.find_element_by_xpath("//option[contains(text(),'5')]")
option.click()

textarea = navegador.find_element_by_xpath("//textarea[@id='textarea-input']")
textarea.click()
textarea.send_keys("Olá mundo!!!")

#file = navegador.find_element_by_xpath("//input[@id='file-input']")
#file.click()
#file.send_keys("C:\\Users\ricar\Pictures\gatogit.jpg")

senha = navegador.find_element_by_xpath("//input[@placeholder='Senha']")
senha.click()
senha.send_keys("2w3e4r5t")

radio = navegador.find_element_by_xpath("//input[@id='radios2-input']")
radio.click()

check = navegador.find_element_by_xpath("//label[contains(text(),'Check')]")
check.click()

cadastrar = navegador.find_element_by_xpath("//button[@id='submit-input']")
cadastrar.click()

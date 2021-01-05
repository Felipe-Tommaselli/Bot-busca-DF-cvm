import time, random
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

dia = str(date.today().day)
mes = str(date.today().month)
ano = str(date.today().year)

if date.today().day < 10:
    dia = '0' + dia
if date.today().month < 10:
    mes = '0' + mes
hoje = dia + mes + ano

PATH = r'C:/Users/Tommasellk/FELIPE/bots/chromedriver.exe'

driver = webdriver.Chrome(PATH)

try:
    driver.get('https://cvmweb.cvm.gov.br/SWB/Sistemas/SCW/CPublica/CiaAb/FormBuscaCiaAb.aspx?TipoConsult=c')
except:
    driver.quit()

try: 
    driver.implicitly_wait(10)
    search = driver.find_element_by_xpath('//*[@id="txtCNPJNome"]')
    search.send_keys('JBS SA')
    print("Search done")
    search.send_keys(Keys.RETURN)
except :
    print('não foi possivel pesquisar')

driver.implicitly_wait(10)

try: 
    driver.implicitly_wait(10)
    search = driver.find_element_by_xpath('//*[@id="dlCiasCdCVM__ctl1_Linkbutton1"]').click()
    print("Company click done")
except:
    print('não foi possivel clicar na empresa')

driver.implicitly_wait(10)

try: 
    driver.implicitly_wait(10)
    search = driver.find_element_by_xpath('//*[@id="chkUltimaData"]').click()
    print("ref click done")
except:
    print('não foi possivel clicar na ultima data de ref')

driver.implicitly_wait(10)

try: 
    driver.implicitly_wait(10)
    search = driver.find_element_by_xpath('//*[@id="txtDataIni"]')
    search.send_keys('01122019')  
    print("data init feito")
except:
    print('não foi possivel adicionar data inicial')

driver.implicitly_wait(10)

try: 
    driver.implicitly_wait(10)
    search = driver.find_element_by_xpath('//*[@id="txtDataFim"]')
    search.send_keys(hoje)
    print("data autal feito")
except:
    print('não foi possivel adicionar data de hoje')

driver.implicitly_wait(10)

try: 
    driver.implicitly_wait(10)
    search = driver.find_element_by_xpath('//*[@id="cboCategoria_chosen"]').click() 
    search = driver.find_element_by_xpath('//*[@id="cboCategoria_chosen_input"]')
    search.send_keys('DFP')  
    search.send_keys(Keys.RETURN) 
    print("clique feito")
except:
    print('não foi possivel selecionar a categoria')

driver.implicitly_wait(10)

try: 
    driver.implicitly_wait(10)
    search = driver.find_element_by_xpath('//*[@id="btnConsulta"]').click() 
    print("clique feito")
except:
    print('não foi possivel Consultar')

driver.implicitly_wait(10)

try: 
    driver.implicitly_wait(10)
    search = driver.find_element_by_xpath('//*[@id="grdDocumentos"]/tbody/tr/td[11]/i[2]').click() 
    search = driver.find_element_by_aria('ui-id-159')
    print("clique final feito")
except:
    print('não foi possivel visualizar documento')

time.sleep(10)
driver.quit()

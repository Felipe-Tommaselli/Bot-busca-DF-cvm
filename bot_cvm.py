import time
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

# funçõa que coleta a data atual e formata na forma do site da cvm
def today_date():
    dia = str(date.today().day)
    mes = str(date.today().month)
    ano = str(date.today().year)

    if date.today().day < 10:
        dia = '0' + dia
    if date.today().month < 10:
        mes = '0' + mes 
    return dia + mes + ano

# inputs
   
company = input('Nome da empresa: ')
init_date = input('Data inicial de procura(ddmmaa): ')
if input('Deseja manter a categoria de pesquisa como DFP?(S/N) ').upper() == 'N':
    category = input('Digite o nome da categoria desejada: ')
else:
    category = 'DFP'

PATH = r'C:/Users/Tommasellk/FELIPE/bots/chromedriver.exe'

driver = webdriver.Chrome(PATH)

# Acessa a pagina da cvm

try:
    driver.get('https://cvmweb.cvm.gov.br/SWB/Sistemas/SCW/CPublica/CiaAb/FormBuscaCiaAb.aspx?TipoConsult=c')
except:
    driver.quit()

# Pesquisa o nome da empresa

try: 
    driver.implicitly_wait(10)
    search = driver.find_element_by_xpath('//*[@id="txtCNPJNome"]')
    search.send_keys(company)
    print("Pesquisa da empresa realizada!")
    search.send_keys(Keys.RETURN)
except :
    print('não foi possivel realizar a pesquisa')

driver.implicitly_wait(10)
# Seleciona a empresa (caso haja mais de um sempre a primeira)

try: 
    driver.implicitly_wait(10)
    search = driver.find_element_by_xpath('//*[@id="dlCiasCdCVM__ctl1_Linkbutton1"]').click()
    print("Empresa selecionada!")
except:
    print('não foi possivel selecionar a empresa')

driver.implicitly_wait(10)
# Marca da opção da ultima data de referencia

try: 
    driver.implicitly_wait(10)
    search = driver.find_element_by_xpath('//*[@id="chkUltimaData"]').click()
    print("Ultima data de referencia selecionada")
except:
    print('não foi possivel clicar na ultima data de referencia')

driver.implicitly_wait(10)
# Preenche a data inicial

try: 
    driver.implicitly_wait(10)
    search = driver.find_element_by_xpath('//*[@id="txtDataIni"]')
    search.send_keys(init_date)  
    print("data inicial preenchida")
except:
    print('não foi possivel adicionar data inicial')

driver.implicitly_wait(10)
# Preenche a data de hoje como data final

try: 
    driver.implicitly_wait(10)
    search = driver.find_element_by_xpath('//*[@id="txtDataFim"]')
    search.send_keys(today_date())
    print("data atual preenchida")
except:
    print('não foi possivel adicionar data atual')

driver.implicitly_wait(10)
# Marca a categoria desejada (DFP por default)

try: 
    driver.implicitly_wait(10)
    search = driver.find_element_by_xpath('//*[@id="cboCategoria_chosen"]').click() 
    search = driver.find_element_by_xpath('//*[@id="cboCategoria_chosen_input"]')
    search.send_keys(category)  
    search.send_keys(Keys.RETURN) 
    print("clique feito")
except:
    print('não foi possivel selecionar a categoria')

driver.implicitly_wait(10)
# Realiza a consulta

try: 
    driver.implicitly_wait(10)
    search = driver.find_element_by_xpath('//*[@id="btnConsulta"]').click() 
    print("clique feito")
except:
    print('não foi possivel Consultar')

driver.implicitly_wait(10)

time.sleep(30)

# Depois de 30s de espera pergunta se o usuario quer salvar o .zip padrao
question = input('Deseja salvar os arquivos .zip?(S/N) ').upper()

# Se ele não quiser, o driver é fechado
if question == 'N':
    driver.implicitly_wait(10)
    driver.quit()

# Se ele quiser, o .zip é salvo e o programa é fechado
try: 
    driver.implicitly_wait(10)
    search = driver.find_element_by_xpath('//*[@id="grdDocumentos"]/tbody/tr/td[11]/i[2]').click() 
    search = driver.find_element_by_aria('ui-id-159').click()
    print("clique final feito")
except:
    if question == 'S':
        print('não foi possivel visualizar documento')

driver.quit()
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver import chrome
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def lookAtBanrep():
    driver.get('https://totoro.banrep.gov.co/analytics/saw.dll?Go&path=%2Fshared%2fSeries%20Estad%c3%adsticas_T%2F1.%20Monedas%20disponibles%2F1.1.TCM_Datos%20diarios&Options=rdf&lang=es&NQUser=publico&NQPassword=publico123')
    driver.implicitly_wait(20)
    pesos = Select(driver.find_element_by_xpath('/html/body/table/tbody/tr/td/div/div[1]/table/tbody/tr[3]/td/table/tbody/tr/td/div/table/tbody/tr[1]/td/table/tbody/tr/td[1]/table/tbody/tr/td[3]/table/tbody/tr/td[3]/select'))
    pesos.select_by_value("6")  
    sleep(2)
    typeOfRate = Select(driver.find_element_by_xpath('/html/body/table/tbody/tr/td/div/div[1]/table/tbody/tr[3]/td/table/tbody/tr/td/div/table/tbody/tr[1]/td/table/tbody/tr/td[2]/table/tbody/tr/td[3]/table/tbody/tr/td[3]/select'))
    typeOfRate.select_by_value("8")
    sleep(2)
    value=driver.find_element_by_xpath('/html/body/table/tbody/tr/td/div/div[1]/table/tbody/tr[3]/td/table/tbody/tr/td/div/table/tbody/tr[3]/td/table/tbody/tr[17]/td[3]')
    reading=value.text
    reading=reading.replace(".","")
    reading=reading.replace(",",".")
    rate=float(reading)
    driver.close()
    return rate

def lookAtProcredit():
    driver.get('https://ebanking.bancoprocredit.com.co/User/LogOn')
    driver.implicitly_wait(5)
    username=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/input')
    username.send_keys("XXXXXXXXXXX") #Insert CC number or Procredit UserName here
    driver.implicitly_wait(1)
    password=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/input')
    password.send_keys("XXXXXXXXXXXX") # Insert Password here
    driver.implicitly_wait(1)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/div[2]/div/input').click()
    driver.implicitly_wait(2)
    balance=driver.find_element_by_xpath('/html/body/div[1]/div[2]/table[1]/tbody/tr/td[6]').text
    driver.find_element_by_xpath('/html/body/header/div/div[2]/div[2]/a[2]').click()
    balance=balance.replace(".","")
    balance=balance.replace(",",".")
    correctedBalance=float(balance)-5000 #Calculation based on the fact they charge 5000 for each withdrawal
    return correctedBalance


print("Web-Scrapper for Balance verification and conversion from ProCredit Colombia - Germany Blocked Accounts using rates from Banco de la Republica de Colombia")

opt = Options()
opt.add_argument('disable-extensions')
opt.add_argument("no-proxy-server")
opt.add_argument("disable-infobars")
opt.add_experimental_option('excludeSwitches', ['enable-logging'])
opt.headless = True
try:
    driver = webdriver.Chrome('chromedriver.exe', options=opt)
except:
    print("Consider updating the chromedriver to make this process faster")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
    
driver.implicitly_wait(2)

balance=lookAtProcredit()
print('Your current balance in Procredit is {0} COP'.format(balance+5000))
convert=input('Do you wanna convert it to EUR (y/n) -> ')
if convert=='y':
    rate=lookAtBanrep()
    print('Todays Sell Rate: {0}'.format(rate))
    balanceEU=balance/rate
    print("Available balance in EUR (5000 COP for transaction, already accounted): ", balanceEU)
else:
    driver.quit()
    exit()


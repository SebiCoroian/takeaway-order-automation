from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
import requests

#WEB DRIVER SET-UP
PATH = "C:\Program Files (x86)\chromedriver.exe"
c = wd.ChromeOptions()
c.add_argument("--incognito")
driver = wd.Chrome(executable_path=PATH,options=c)

#TEMPMAIL API SET-UP
url = "https://privatix-temp-mail-v1.p.rapidapi.com/request/delete/id/%7Bmail_id%7D/"
headers = {
    'x-rapidapi-host': "privatix-temp-mail-v1.p.rapidapi.com",
    'x-rapidapi-key': "SIGN-UP-FOR-KEY"
    }
response = requests.request("GET", url, headers=headers)
print(response.text)

#VARIABLE SET-UP
#USER CONFIG
restaurant_url = ""
e-mail = requests.request("GET", url, mail_id)
adress = ""
name = ""
phone = ""
voucher = ""
card_number = ""
exp_dare = ""
cvv = ""

#START
driver.get(restaurant_url)
driver.implicitly_wait(5)

#PRODUCT SELECTION
prod T=driver.find_elements_by_xpath("//*[contains(text(), 'YOUR PRODUCT NAME')]")
driver.execute_script("arguments[0].scrollIntoView();", prod[0])
prod[0].click()
driver.implicitly_wait(5)

ADRESS_BLOCK = driver.find_element_by_xpath("//label[1]")
ADRESS_BLOCK.send_keys(adress)
ADRESS_BLOCK.send_keys(Keys.RETURN)
driver.implicitly_wait(5)

ATC = driver.find_element_by_class_name("_1k89- _16ivD _3VIvy eINXa _3tciV _1dOib")
ATC.click()
driver.implicitly_wait(5)

CKOUT = driver.find_element_by_class_name("_1k89- _16ivD _3VIvy eINXa _3tciV _1dOib")
CKOUT.click()
driver.implicitly_wait(5)

FIELDS = driver.find_elements_by_xpath("//label[]")
FIELDS[9].send_keys(name)
FIELDS[10].send_keys(email)
FILDS[11].send_keys(phone)
driver.implicitly_wait(5)

VOUCHER = driver.find_elements_by_partial_link_text("Add a voucher")
VOUCHER.click()
driver.implicitly_wait(5)

VOUCHER_BOX = driver.find_element_by_xpath("//label[1]")
VOUCHER_BOX.send_keys(voucher)
VOUCHER_BOX.send_keys(Keys.RETURN)
driver.implicitly_wait(5)

PAY = driver.find_elements_by_xpath("//*[contains(text(), 'Pay with')]")
PAY.click()
CC = driver.find_elements_by_xpath("//div[@label='Creditcard']")
CC.click()
DONE = driver.find_element_by_class_name("_1k89- _16ivD _3VIvy eINXa _3tciV _1dOib")
DONE.click()
driver.implicitly_wait(5)

ORDER = driver.find_element_by_class_name("_1k89- _16ivD _3VIvy eINXa _3tciV _1dOib")
ORDER.click
driver.implicitly_wait(5)

CARD_FIELDS = driver.find_elements_by_xpath("//label[]")
CARD_FIELDS[0] = card_number
CARD_FIELDS[1] = exp_date
CARD_FIELDS[2] = cvv
CARD_FIELDS[3] = name
driver.implicitly_wait(5)

PAYMENT = find_element_by_class_name ("form-actions")
PAYMENT.click()
driver.implicitly_wait(5)

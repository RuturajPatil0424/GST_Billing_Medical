from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")

no="8830136942"
filepath= "../GSTInvoices/Ruturaj_4562.pdf"
sleep(30)
# user = driver.find_element()

sleep(30)
# driver.find_element(by=By.XPATH,value='//div[@title = "Attach"]').click()
driver.find_element(by=By.XPATH,value='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div').click()
sleep(30)
driver.find_element(by=By.XPATH,value='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[4]/button').click()





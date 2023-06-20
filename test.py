from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
import pywhatkit
import datetime
import webbrowser
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver
import pandas as pd
from Body.Say import say
import pathlib
from Body.Listen import Command


scriptDirectory = pathlib.Path().absolute()

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--profile-directory=Default")
options.add_argument(f"user-data-dir={scriptDirectory}\\userdata")
Options.headless = True
os.system("")
os.environ["WDM_LOG_LEVEL"] = "0"
PathofDriver = "DataBase/chromedriver.exe"
driver = webdriver.Chrome(PathofDriver, options=options)
driver.maximize_window()
driver.get("https://web.whatsapp.com/")





def WhatsappSender(Name):


    Number = "8830136942"
    LinkWeb = 'https://web.whatsapp.com/send?phone=' + Number + "&text="
    driver.get(LinkWeb)
    sleep(5)
    try:
        driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()
        say("Message Sent")

    except:
        print("Invalid Number")


def whatsapp(Data):
    if "send whatsapp message" in Data:
        Task = str(Data).lower()
        Namen = str(Task).replace("send", "")
        Namen = str(Namen).replace("whatsapp", "")
        Namen = str(Namen).replace("message", "")
        Namen = str(Namen).replace("to ", "")
        Namen = str(Namen).replace(" ", "")
        WhatsappSender(Namen)

    elif "send a whatsapp message" in Data:
        Task = str(Data).lower()
        Namen = str(Task).replace("send", "")
        Namen = str(Namen).replace("whatsapp", "")
        Namen = str(Namen).replace("message", "")
        Namen = str(Namen).replace("to ", "")
        Namen = str(Namen).replace("a", "")
        Namen = str(Namen).replace(" ", "")
        WhatsappSender(Namen)


# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# import os
# import pywhatkit
# import datetime
# import webbrowser
# from bs4 import BeautifulSoup
# from time import sleep
# from selenium import webdriver
# import pandas as pd
# import pathlib
#
#
#
# scriptDirectory = pathlib.Path().absolute()
#
# options = Options()
# options.add_experimental_option("excludeSwitches", ["enable-logging"])
# options.add_argument("--profile-directory=Default")
# options.add_argument(f"user-data-dir={scriptDirectory}\\userdata")
# Options.headless = True
# os.system("")
# os.environ["WDM_LOG_LEVEL"] = "0"
# PathofDriver = "DataBase/chromedriver.exe"
# driver = webdriver.Chrome(PathofDriver, options=options)
# driver.maximize_window()
# driver.get("https://web.whatsapp.com/")
#
#
#
#
#
# def WhatsappSender(Name):
#
#
#     Number = "8830136942"
#     LinkWeb = 'https://web.whatsapp.com/send?phone=' + Number + "&text="
#     driver.get(LinkWeb)
#     sleep(5)
#     try:
#         driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()
#         # say("Message Sent")
#
#     except:
#         print("Invalid Number")
#
#
# def whatsapp(Data):
#     if "send whatsapp message" in Data:
#         Task = str(Data).lower()
#         Namen = str(Task).replace("send", "")
#         Namen = str(Namen).replace("whatsapp", "")
#         Namen = str(Namen).replace("message", "")
#         Namen = str(Namen).replace("to ", "")
#         Namen = str(Namen).replace(" ", "")
#         WhatsappSender(Namen)
#
#     elif "send a whatsapp message" in Data:
#         Task = str(Data).lower()
#         Namen = str(Task).replace("send", "")
#         Namen = str(Namen).replace("whatsapp", "")
#         Namen = str(Namen).replace("message", "")
#         Namen = str(Namen).replace("to ", "")
#         Namen = str(Namen).replace("a", "")
#         Namen = str(Namen).replace(" ", "")
#         WhatsappSender(Namen)
#
#

# books = [
# ['123', 'book1', 25],
# ['243', 'book2', 30],
# ['874', 'book3', 15],
# ['519', 'book4', 20],
# ['745', 'book5', 10]
# ]
#
# # Use sort() method if you don't need to create a new object
# books.sort(key=lambda x : x[2])
# print(books)
#
# # Use sorted() function if you want a new object
# sorted_books = sorted(books, key=lambda x: x[2])
# print(sorted_books)

from openpyxl import Workbook

# Create a new workbook
wb = Workbook()
sheet = wb.active

# Add column headers
sheet.append(['Name', 'Tax Amount', 'GST Rate', 'GST Amount'])

# Add sample tax data with GST
tax_data = [
    ['John Doe', 1000, "18", '=B2*C2/100'],
    ['Jane Smith', 1500, "12", '=B3*C3/100'],
    ['Mike Johnson', 800, "5", '=B4*C4/100']
]
s=tax_data.sort(key=lambda x : x[2])
print(tax_data)

for data in tax_data:
    sheet.append(data)

# Save the workbook
wb.save('gst_tax_data.xlsx')
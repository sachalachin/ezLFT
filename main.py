import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import tkinter as tk
from tkinter import messagebox
from dotenv import load_dotenv


print("""
               _        ______   _______
              | |      |  ____| |__   __|
   ___   ____ | |      | |__       | |
  / _ \ |_  / | |      |  __|      | |
 |  __/  / /  | |____  | |         | |
  \___| /___| |______| |_|         |_|                                        

by Sacha Lachin 
""")

# Import NHS login credentials from .env file
load_dotenv()
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")



# Create options object and configure chrome to operate in headless mode (without GUI)
service = Service('./chromedriver')
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(service=service, options=options)

# Set implicit wait to 10 seconds to allow elements enough time to load
driver.implicitly_wait(10)

# Load starting page and proceed through order process
driver.get("https://www.gov.uk/order-coronavirus-rapid-lateral-flow-tests")
print("1. Portal loaded")
driver.find_element(By.XPATH, "//a[contains(.,'Start now')]").click()
driver.find_element(By.ID, "condition-2").click()
driver.find_element(By.XPATH, "//button[normalize-space()='Continue']").click()
print("2. No current symptoms")
driver.find_element(By.XPATH, "//button[@class='govuk-button govuk-button--secondary']").click()
print("3. Proceeding to NHS login")

# Login through NHS - I have not seen them use a Captcha system, but this will break should one be introduced
emailField = driver.find_element(By.ID, "user-email")
emailField.send_keys(EMAIL)
emailField.submit()
driver.find_element(By.XPATH, "//button[@class='nhsuk-button']").click()
passField = driver.find_element(By.ID, "password-input")
passField.send_keys(PASSWORD)
passField.submit()
print("4. Login Success")

driver.find_element(By.ID, "nhs-staff-2").click()
driver.find_element(By.XPATH, "//button[normalize-space()='Continue']").click()
print("5. Not part of NHS staff testing")
driver.find_element(By.XPATH, "//button[normalize-space()='Save and continue']").click()
print("6. Details exist")
driver.find_element(By.XPATH, "//input[@name='disclaimer']").click()
print("7. Agreed to disclaimer")
address = driver.find_element(By.CSS_SELECTOR, "td.sc-fzoPby.SpZXO").text
print("8. Opening confirmation prompt ")


# GUI popup asking for confirmation prior to order
root = tk.Tk()
root.iconbitmap(default="favicon.ico")
root.withdraw()
ConfirmBox = messagebox.askquestion("Confirm Order",
                                        "Do you want to order a box of lateral flow tests to:\n" + address)
if ConfirmBox == "yes":
    # Order LFTs
    driver.find_element(By.ID, "7-submit-order").click()
    messagebox.showinfo("Order Success", "Your box of 7 lateral flow tests has been ordered.")
    print("9. Order success")
else:
    root.destroy()
    print("Cancelled")







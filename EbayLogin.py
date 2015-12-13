from selenium.webdriver.common.by import By
from selenium import webdriver
from config import EbayConfigUtil

ebay_url = "https://ebay.com"

"""
Logs the user into Ebay
@param browser: Selenium Web Driver instance
"""
def login(browser):    
  
    browser.get(ebay_url)

    #navigate to sign in page
    sign_in_link = browser.find_element(By.CSS_SELECTOR, "#gh-ug a")
    sign_in_link.click()
    
    #get user credentials
    username_input = browser.find_element(By.ID, "userid")
    password_input = browser.find_element(By.ID, "pass")

    #enter user credentials into form
    username_input.send_keys(EbayConfigUtil.getUsername())
    password_input.send_keys(EbayConfigUtil.getPassword())

    #submit form and redirect to main page
    submit = browser.find_element(By.CSS_SELECTOR, "input[type='submit']")
    submit.click()
    






if __name__ == "__main__":
    login(webdriver.Firefox())
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    
    #get user credential elements in form
    inputs = browser.find_elements(By.TAG_NAME, "input")
    username_input, password_input = _findUserAndPassInputs(inputs)

    print username_input.get_attribute("id")
    print password_input.get_attribute("id")

    #enter user credentials into form
    username_input.send_keys(EbayConfigUtil.getUsername())
    password_input.send_keys(EbayConfigUtil.getPassword())

    #submit form and redirect to main page
    submit = browser.find_element(By.CSS_SELECTOR, "input[type='submit']")
    submit.click()
    

"""
Find the (first) username and password inputs of a page, given all <input>s on the page
@param inputs: All input tag elements
@returns (username element, password element): The username and password elements
"""
def _findUserAndPassInputs(inputs):
    import re

    uname_input = None
    pass_input = None

    uname_regex = re.compile(r"(user(_| )?(name)?(id)?)|(email(_| )?(address)?)", re.IGNORECASE)    #match user, user id, user name, email, email address variants
    pass_regex = re.compile(r"pass(word)?", re.IGNORECASE)

    #Since Ebay literally went straight fuckboi, we have to make a ton of hacky checks to actually find "real" input elements
    valid_inputs = [x for x in inputs if x.get_attribute("placeholder") and x.size and (x.location['x'] > 2 or x.location['y'] > 2)]
    for i in valid_inputs:
        if uname_input and pass_input: break

        placeholder_val = i.get_attribute("placeholder")

        if uname_regex.search(placeholder_val):
            uname_input = i

        elif pass_regex.search(placeholder_val):
            pass_input = i


    return (uname_input, pass_input)



def main():
    login(webdriver.Firefox())

if __name__ == "__main__":
    main()
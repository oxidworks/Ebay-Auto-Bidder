from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
"""
Collects the various information from the item web page for the script. 
"""
class EbayPageScraper(object):

    def __init__(self, url, browser = None):
        self.browser = browser if browser else webdriver.Firefox()
        self.URL = url;

        if self.browser.current_url is not url:
            self.browser.get(self.URL)

    """
    Gets the current price of the item by scraping the data from the site
    @return (float): Item price in decimal form 
    """
    def getCurrentPrice(self):
        price_ele = self.browser.find_element(By.XPATH, "//span[@itemprop='price']")
        price_text = price_ele.text     #will be of form 'US $xxx.xxx'

        #parse price_text for actual float price
        price = price_text.split("$")[1]
        return float(price)


    """
    Gets the description of the item by scraping the data from the site
    @return (string): description
    """
    def getDescription(self):
        descrip_element = self.browser.find_element(By.ID, "itemTitle")
        return descrip_element.text


    """
    Gets the auction end time of the item by scraping the data from the site
    @return (long): The end time of the auction in millisecond representation
    """
    def getEndTime(self):
        end_time_element = self.browser.find_element(By.XPATH, "//span[@class='timeMs']")
        end_time = end_time_element.get_attribute("timems")

        return long(end_time)       #returns it in milliseconds, which can be parsed and translated into a readable date



if __name__ == "__main__":
    pass

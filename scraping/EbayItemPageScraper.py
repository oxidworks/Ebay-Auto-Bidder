from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import re

"""
Collects the various information from the item web page for the script. 
"""
class EbayItemPageScraper(object):

    def __init__(self, browser):
        assert isinstance(browser, WebDriver)
        self.browser = browser

 
    """
    Returns an object that refers to the autobid button on the EBay item page. 
    @param browser: Browser instance already displaying the eBay item page
    @return (<input>, <button>): The autobid button on the page that can be clicked
    """
    
    def getAutoBidInputAndButton(self):
        assert isinstance(browser, WebDriver)

        #Find the auto bid input by finding the label indicating max bid and taking the input below it
        all_labels = self.browser.find_elements(By.TAG_NAME, "label")

        bid_label_pattern = re.compile(r"(max)? ?bid")

        

        

            


    
    """
    Gets the current price of the item by scraping the data from the site
    @params browser: Browser instance already displaying the eBay item page
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
    @params browser: Browser instance already displaying the eBay item page
    @return (string): description
    """
    
    def getDescription(self):
        descrip_element = self.browser.find_element(By.ID, "itemTitle")
        return descrip_element.text


    """
    Gets the auction end time of the item by scraping the data from the site
    @params browser: Browser instance already displaying the eBay item page
    @return (long): The end time of the auction in millisecond representation
    """
    
    def getEndTime(self):
        end_time_element = self.browser.find_element(By.XPATH, "//span[@class='timeMs']")
        end_time = end_time_element.get_attribute("timems")

        return long(end_time)       #returns it in milliseconds, which can be parsed and translated into a readable date



    """
    Gets the main form element which contains all relevant information for the page scraper. 
    @param browser: Browser instance already displaying the eBay item page
    @return <form>: The main form item from the item auction page
    """
    
    def getMainContentForm(self):
        #Main form containing all relevant details follows this template: <form action ="www.offer.ebay.com/..."  ...>
        main_form = self.browser.find_element(By.XPATH, "//form[contains(@action, 'offer.ebay')]")    
        
        return main_form










def test():
    item_url = raw_input("Enter the url of an Ebay Auction Item: ")

    browser = webdriver.Firefox()
    browser.get(item_url)
    scraper = EbayItemPageScraper(browser)
    
    print "Current price of item: %0.3f\n" % scraper.getCurrentPrice()
    print "Item description: %s\n" % scraper.getDescription()
    print "Auction ends at: %d\n" % scraper.getEndTime()


if __name__ == "__main__":
    test()
    

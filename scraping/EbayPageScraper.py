from selenium import webdriver
from selenium.webdriver.common import keys
"""
Collects the various information from the item web page for the script. 
"""
class EbayPageScraper(object):

    def __init__(self, url, browser = None):
        if not browser:
            browser = webdriver.Firefox()
        self.URL = url;
        self.description


    """
    Gets the current price of the item by scraping the data from the site
    """
    def getCurrentPrice():
        pass

    """
    Gets the description of the item by scraping the data from the site
    """
    def getDescription():
        pass

    """
    Gets the auction end time of the item by scraping the data from the site
    """
    def getEndTime():
        pass



    if __name__ == "__main__":
      

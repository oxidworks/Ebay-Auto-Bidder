"""
This module contains all the functionality for interacting with the Ebay website,
including browser automation, login and storage of credentials, and automated bidding.
@author Naveen Chandran
"""

from selenium import webdriver
from scraping import EbayPageScraper
from models import AuctionItem

class EbayBot():
    
#     Class hash map that contains information about items. Keys are the item names (string) 
#     and Values are tuples of pertinent information about the item
#     EX: item_map["ball"] -> (url, maximum bid, end time)
    item_info = {} 
    
    
    
    
    
    def __init__(self):
        pass
    
    """
    This is the main callable method of the class that monitors an item until it gets down to the last 
    few seconds, and then places an autobid if it isn't already higher than the user's maximum bid amount.
    @param item_url:   The item url of form http://www.ebay.com/xxx/...
    @param max_bid:    The maximum amount the user is willing to pay for the item
    """
    def monitor(self, item_url, max_bid):
        self.__add_item_from_URL(item_url)
        pass
    








    """
    ************************************************
    ****************PRIVATE METHODS****************
    ************************************************
    """
    def __add_item_from_URL(self, url):
        scraper = EbayPageScraper()
        descrip = scraper.getDescription()
        end_time = scraper.getEndTime()
        curr_price = scraper.getCurrentPrice()

        item = AuctionItem(descrip, scraper.URL, end_time, curr_price)

        return scraper, item
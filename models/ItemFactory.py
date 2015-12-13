from selenium import webdriver
from Item import Item

"""
Constructs an item object given the URL.
"""
class ItemFactory(object):


    @staticmethod
    def createItem(url):
        current_price = getCurrentPrice(url)
        description = getDescription(url)
        end_time = getEndTime(url)

        return Item(url, end_time, current_price, description)









#################################################################
#                    PRIVATE HELPER METHODS                     #
#################################################################


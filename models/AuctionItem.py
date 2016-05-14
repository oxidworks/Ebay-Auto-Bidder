"""
This class represents an item that is being monitored for bidding
"""
class AuctionItem(object):

    def __init__(self, description, url, end_time, current_price):
        self.description = description
        self.URL = url
        self.end_time = end_time
        self.current_price = current_price
        self.user_max_bid = 0


    def setUserMaxBid(self, bid):
        self.user_max_bid = bid




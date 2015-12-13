"""
This class represents an item that is being monitored for bidding
"""
class Item(object):

    def __init__(self, url, end_time, current_price, description = None):
        self.URL = url
        self.end_time = end_time
        self.description = description
        self.current_price = 0
        self.max_bid_price = 0
 




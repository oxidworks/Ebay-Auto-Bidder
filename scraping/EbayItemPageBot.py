

"""
Collects the various information from the item web page for the script. 
"""
class EbayItemPageBot(object):

    def __init__(self, url, browser = None):
        self.browser = browser if browser else webdriver.Firefox()
        self.URL = url;

        if self.browser.current_url is not url:
            self.browser.get(self.URL)

   
            
            
            
            
            
            
            
            
            
            
            
            
            
                 
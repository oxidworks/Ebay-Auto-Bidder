"""
Extends the default Selenium Web Driver to incorporate tabs and switching between them
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TabbedFirefoxDriver(webdriver.Firefox):
    def __init__(self):
        super(TabbedFirefoxDriver, self).__init__()

        #Array of tab names. Tab_names[i] is the name of the ith tab
        self._tab_names = []
        self._tab_names.append("@init")   #tab 0 is always initially named @init

        self.curr_tab = 0

    """
    Removes the given tab from the browser
    @param name: The tab name to remove
    @return None
    """
    def removeTab(self, name):
        self.switchToTab(name);
        self.find_element(By.TAG_NAME, "body").send_keys(Keys.CONTROL + "w")

        index = self._tab_names.index(name)
        del self._tab_names[index]

        #if we removed the last tab, our tab number goes down, otherwise we are on the same tab position
        if index == self.getNumTabs()-1:
            self.curr_tab -= 1

        

    """
    Returns a tuple of the current tab number and its name
    @return (tab number, tab name)
    """
    def getCurrTab(self):
        return self.curr_tab, self._tab_names(self.curr_tab)

    """
    Switches to the tab with the specified name. Returns the current tab number and name after execution
    @param name: The tab name to switch to
    @return (current tab number, current tab name)
    """
    def switchToTab(self, name):
        index = self._tab_names.index(name)
        num_tabs_to_switch = (index + self.curr_tab) % self.getNumTabs()
        for i in range(index):
            number, name = self._switchOneTab()

        return number, name

    """
    @private
    Switches one tab in the browser and returns the current tab number and name after execution
    @return (tab number, tab name)
    """
    def _switchOneTab(self):
        self.find_element(By.TAG_NAME, "body").send_keys(Keys.CONTROL + Keys.TAB)
        self.curr_tab = (self.curr_tab + 1) % self.getNumTabs()
        return self.getCurrTab()

    """
    Creates a new tab in the current browser instance
    @param name: The unique name of the tab to be created 
    """
    def createTab(self, name, url=None):
        #open a new tab
        self.find_element(By.TAG_NAME, "body").send_keys(Keys.CONTROL + "t")

        #navigate to url, if provided
        if url:
            self.get(url)

        #increase number of tabs open and add name to array
        self._tab_names.append(name)


    """
    Returns the number of tabs presently open in the browser
    @return A tuple of values (tab number, tab name)
    """
    def getTabs(self):
        return self._tab_names

    def getNumTabs(self):
        return len(self._tab_names)


if __name__ == "__main__":
    d = TabbedFirefoxDriver()
    print d.getTabs()

        




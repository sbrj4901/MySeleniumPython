import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

class listhandle:
    driver = webdriver.Chrome("c:\selenium browse drivers\chromedriver.exe")
    def listhandle(self,actualtext):
        self.driver.get("http://www.makemytrip.com/")
        Next=self.driver.find_element_by_id("fromCity")
        Next.click()
        totalvalue = self.driver.find_elements_by_xpath("//ul[@role='listbox']//li")
        sizeofrowlist=len(totalvalue)
        for x in range(1,sizeofrowlist):
            text_value = self.driver.find_element_by_xpath("//ul[@role='listbox']//li["+str(x)+"]//div[2]").text
            if text_value == actualtext:
                self.driver.find_element_by_xpath("//ul[@role='listbox']//li["+str(x)+"]").click()
                break
obj=listhandle()
obj.listhandle("HYD")
from selenium import webdriver
# from selenium.webdriver.support.select.import Select

class webtab:
    driver = webdriver.Chrome("C:\selenium browse drivers\chromedriver.exe")
    def table(self):
        self.driver.get("http://www.leafground.com/pages/table.html")
        totalrowvalue = self.driver.find_elements_by_xpath("//table[@id='table_id']//tr")
        sizeofrowlist = len(totalrowvalue)
        print(sizeofrowlist)

W = webtab()
W.table()

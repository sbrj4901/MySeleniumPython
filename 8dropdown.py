import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

class dpwon:
    driver = webdriver.Chrome('C:\selenium browse drivers\chromedriver.exe')

    def dropdown(self,a,b):
        # c = a + b
        # print(c)
        self.driver.get("http://www.leafground.com/pages/Dropdown.html")
        daydropwn = Select(self.driver.find_element_by_id(('dropdown1')))
        daydropwn.select_by_index(3) # For this Purpose we import Select
        monthdropwn = Select(self.driver. find_element_by_name("dropdown2"))
        monthdropwn.select_by_value("4")
        yeardropwn = Select(self.driver.find_element_by_id("dropdown3"))
        yeardropwn. select_by_visible_text("Appium")
    def multiselectdropdown(self):
        self.driver.get('http://www.leafground.com/pages/Dropdown.html')
        # daydropwn = Select(self . driver.find_element_by_id("dropdown1"))
        # daydropwn .select_by_index(2)
        value = Select(self.driver.find_element_by_xpath("(//div[@class='example'][6]//child::select)"))
        multiselect = value.is_multiple
        print(multiselect)
        if multiselect == True:
            print("inside the if")
            value.select_by_index(1)
            value.select_by_value("1")
            value.select_by_visible_text("Selenium")
            value . select_by_visible_text("Appium")
            time.sleep(5)
            value.deselect_all()

    #example for class function
    def addtion(self, a, b):
        c = a + b
        print(c)

obj=dpwon()
obj.dropdown(1,2)
obj.multiselectdropdown()
obj.addtion(10,2)

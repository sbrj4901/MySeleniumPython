import time
from selenium import webdriver
class  dpwon():
    driver = webdriver.Chrome("C:\selenium browse drivers\chromedriver.exe")

    def Alert(self):
        self.driver.get("http://www.leafground.com/pages/Alert.html")
        self.driver.find_element_by_xpath("//button[text()='Alert Box']").click()
        # time.sleep(3)
        self.driver.switch_to.alert.accept()
        self.driver.find_element_by_xpath("//button[text()='Confirm Box']").click()
        self.driver.switch_to.alert.dismiss()
        self.driver.find_element_by_xpath("//button[text()='Prompt Box']").click()
        a=self.driver.switch_to.alert
        a.send_keys("Besant Technologies")
        print(a.text)
        # time.sleep(3)
        a.accept()
        self.driver.find_element_by_xpath("//button[text()='Sweet Alert']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[text()='OK']").click()
    def verification(self):
        self.driver.get("http://www.leafground.com/pages/radio.html")
        # Get Title
        print(self.driver.title)
        # Get current URL
        print(self.driver.current_url)
        # Get Attribute
        classattributename = self.driver.find_element_by_id("yes"). get_attribute('class')
        print(classattributename)
        # Get text
        classattributename = self.driver.find_element_by_id("yes").text
        print(classattributename)
        #CurrentWindowName
        classattributename = self.driver.current_window_handle
        print(classattributename)

    def validation(self):
        self.driver.get("http://www.leafground.com/pages/checkbox.html")
        time.sleep(3)
        print(self.driver.find_element_by_xpath
        ("(//input[@type='checkbox'])[1]").is_displayed()) #its return only boolean statement
        print(self.driver.find_element_by_xpath
        ("(//input[@type='checkbox'])[6]").is_selected()) #its return only boolean statement
        value = self. driver.find_element_by_xpath("(//input[@type= 'checkbox'])[6]").is_selected()
        if value == True:
            self.driver.find_element_by_xpath("(//input[@type='checkbox'])[6]").click()
        print(self.driver.find_element_by_xpath("(//input[@type='checkbox'])[6]").is_enabled())

obj = dpwon()
# obj.Alert()
# obj.verification()
obj.validation()
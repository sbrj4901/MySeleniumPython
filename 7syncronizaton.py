from selenium import webdriver
class sync:
    driver = webdriver . Chrome("C:\selenium browse drivers\chromedriver.exe")
    def sync1(self):
        self.driver.get("https://www.facebook.com/")
        self.driver.find_element_by_xpath("//a[text()='Create New Account']").click()
        self.driver . implicitly_wait(30)
        self.driver .find_element_by_name("firstname").send_keys("subaraj")
        self.driver.find_element_by_name("lastname").send_keys("s")
        self.driver.find_element_by_name('reg_email__').send_keys('sbrj4901')
        self.driver.find_element_by_name('reg_passwd__').send_keys("9876543210")

obj=sync()
obj.sync1()

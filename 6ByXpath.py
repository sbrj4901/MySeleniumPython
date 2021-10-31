from selenium import webdriver
driver = webdriver . Chrome("c:\selenium browse drivers\chromedriver.exe")
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.find_element_by_xpath("//a[text()='Create New Account']").click()
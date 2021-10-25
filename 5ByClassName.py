from selenium import webdriver
driver = webdriver.Firefox(executable_path="c:\selenium browse drivers\geckodriver.exe")
driver.get("https://www.testandquiz.com/selenium/testing.html")
driver . maximize_window()
driver.find_element_by_class_name('Automation').click()
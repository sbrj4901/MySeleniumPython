from selenium import webdriver
driver = webdriver.Firefox(executable_path ='C:\selenium browse drivers\geckodriver.exe' )
driver.get('https://www.testandquiz.com/selenium/testing.html')
# driver.find_element_by_link_text("This is a link").click()
driver . find_element_by_partial_link_text("a link").click()
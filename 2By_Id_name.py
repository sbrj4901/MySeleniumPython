from selenium import webdriver
driver = webdriver.Firefox(executable_path="c:\selenium browse drivers\geckodriver.exe")
driver.get("http://facebook.com")
driver . maximize_window()
# driver. set_window_size(200,300)
# driver.refresh();
# driver.get("http://gmail.com")
# driver.back();
# driver.forward()
username = driver.find_element_by_id('email')
username . send_keys('Subaraj S')
password = driver . find_element_by_id("pass")
password . send_keys('Sbrj4902')
driver.find_element_by_name("login").click()



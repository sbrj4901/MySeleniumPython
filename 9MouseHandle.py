from datetime import time
from selenium import webdriver
from selenium.webdriver import ActionChains
import pyautogui
from selenium.webdriver.common.keys import Keys


class Mousehandle:
    driver = webdriver.Chrome("c:\selenium browse drivers\chromedriver.exe")
    def mouse(self):
        self.driver.get("http://www.leafground.com/pages/mouseOver.html")
        self.driver.maximize_window()
        elec = self.driver.find_element_by_xpath("//a[text()='TestLeaf Courses']")
        ac = ActionChains(self.driver)
        ac.move_to_element(elec).click_and_hold().release().move_to_element(self.driver.find_element_by_xpath
        ("//a[text()='WebServices']")).click().perform()

    def facebook(self):
        self.driver.get("https://en-gb.facebook.com/")
        username = self.driver.find_element_by_id("email")
        ac = ActionChains(self.driver)
        ac.move_to_element(username).send_keys("Subaraj").double_click().context_click().perform()
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('enter')
        pyautogui.press('tab')
        pyautogui.hotkey('ctrl','v')



obj = Mousehandle()
obj.mouse()
# obj.facebook()


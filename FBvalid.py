"""
Author: Sivan Haba
Python Selenium Final Project
First Test: Try log in to Facebook with valid details
"""

from selenium import webdriver
import time
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options



class FBvalid:

    def __init__(self):
        print('FBvalid Test Started')


    def WriteToLog(self, TestFileName, Text):
        f = open(TestFileName, 'a') # open file to get text
        TimeStamp = str(datetime.datetime.now()) # builtin function from datetime module to get current time
        f.write(TimeStamp + " " + Text + '\n') # write timestamp and text, \n to a new line
        f.close() # close file

    def FB_log_in_valid_details_test(self):
        self.TestFileName = "FB_log_in_valid_details_Log.txt"
        self.ResultFile = "Test_Result.txt"
        self.WriteToLog(self.TestFileName, "Start with FB login with valid details TEST")
        self.WriteToLog(self.ResultFile, "Start with FB login for final report:")



        try:
            option = Options()
            option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 1})  # 1 yes 2 No
            self.driver = webdriver.Chrome(options=option, executable_path="C:\\Users\\sivan\\PycharmProjects\\SivPyProjects\\chromedriver.exe")
            self.driver.get("http://www.facebook.com") # open facebook in browser
            self.driver.maximize_window() # maximize window


        except:
            self.WriteToLog(self.TestFileName, "ERROR Occurred During FB Home Page Upload")
            self.WriteToLog(self.ResultFile, "FBvalid Test failed")



        # locate email field and enter valid email address
        try:
            WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.NAME, 'email'))).clear()
            WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.NAME, 'email'))).send_keys('sivikb1985@gmail.com')
            self.WriteToLog(self.TestFileName, "Email field found and valid email address was entered successfully")

        except:
            self.WriteToLog(self.TestFileName, "ERROR - Email field NOT found")
            self.WriteToLog(self.ResultFile, "FBvalid Test failed")



        # locate password field and enter valid password
        try:
            WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.NAME, 'pass'))).send_keys('1985sivikb')
            self.WriteToLog(self.TestFileName, "Password field found and valid password was entered successfully")

        except:
            self.WriteToLog(self.TestFileName, "ERROR - Password field NOT found")
            self.WriteToLog(self.ResultFile, "FBvalid Test failed")



        # locate and click on login button
        try:
            WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, 'loginbutton'))).click()
            self.WriteToLog(self.TestFileName, "Success!!! login button found and pressed successfully - now logged in with valid details")
            self.WriteToLog(self.ResultFile, "FBvalid Test Passed")
            self.driver.get_screenshot_as_file("FB Login With Valid Details.png")
            time.sleep(2)

        except:
            self.WriteToLog(self.TestFileName, "ERROR - Can't find Login button")
            self.WriteToLog(self.ResultFile, "FBvalid Test failed")



        self.driver.quit()



################ main program - use to run from this file #################
#FirstTest = FBvalid()
#FirstTest.FB_log_in_valid_details_test()

"""
Author: Sivan Haba
Python Selenium Final Project
Second Test: Try log in to Facebook with invalid username
"""

from selenium import webdriver
import time
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


class FBinvalidUSER:
    def __init__(self):
        print('FBinvalidUSER Test Started')

    def WriteToLog(self, TestFileName, Text):
        f = open(TestFileName, 'a') # open file to get text
        TimeStamp = str(datetime.datetime.now()) # builtin function from datetime module to get current time
        f.write(TimeStamp + " " + Text + '\n') # write timestamp and text, \n to a new line
        f.close() # close file

    def FB_log_in_invalid_username_test(self):
        self.TestFileName = "FB_log_in_invalid_username_Log.txt"
        self.ResultFile = "Test_Result.txt"
        self.WriteToLog(self.TestFileName, "Start with FB login with invalid username TEST")
        self.WriteToLog(self.ResultFile, "Start with FB login with invalid username for final report:")



        try:
            option = Options()
            option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 1})  # 1 yes 2 No
            self.driver = webdriver.Chrome(options=option, executable_path="C:\\Users\\sivan\\PycharmProjects\\SivPyProjects\\chromedriver.exe")
            self.driver.get("http://www.facebook.com") # open facebook in browser
            self.driver.maximize_window() # maximize window


        except:
            self.WriteToLog(self.TestFileName, "ERROR Occurred During FB Home Page Upload")
            self.WriteToLog(self.ResultFile, "FBinvalidUSER Test failed")



        # locate email field and enter invalid email address
        try:
            WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.NAME, 'email'))).clear()
            WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.NAME, 'email'))).send_keys('sivikb1985isawesome@gfail.com')
            self.WriteToLog(self.TestFileName, "Email field found and INVALID email address was entered successfully")

        except:
            self.WriteToLog(self.TestFileName, "ERROR - Email field NOT found")
            self.WriteToLog(self.ResultFile, "FBinvalidUSER Test failed")



        # locate password field and enter valid password
        try:
            WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.NAME, 'pass'))).send_keys('1985sivikb')
            self.WriteToLog(self.TestFileName, "Password field found and valid password was entered successfully")


        except:
            self.WriteToLog(self.TestFileName, "ERROR - Password field NOT found")
            self.WriteToLog(self.ResultFile, "FBinvalidUSER Test failed")


        # locate and click on login button
        try:
            WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, 'loginbutton'))).click()
            self.WriteToLog(self.TestFileName, "Login button found and pressed successfully")
            time.sleep(2)

        except:
            self.WriteToLog(self.TestFileName, "ERROR - Can't find Login button")
            self.WriteToLog(self.ResultFile, "FBinvalidUSER Test failed")


        # locate relevant error message element and get text
        try:
            res = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, '//*[@id="globalContainer"]/div[3]/div/div/div'))).text
            print(res)
            if res == "The email you’ve entered doesn’t match any account. Sign up for an account.":
                self.WriteToLog(self.TestFileName, "ERROR MESSAGE APPEARS: The email you've entered doesn't match any account. sign up for an account.")
                self.driver.get_screenshot_as_file("FB Login With Invalid Details.png")
                self.WriteToLog(self.ResultFile, "FBinvalidUSER Test passed")

            else:
                self.WriteToLog(self.TestFileName, "No relevant error message appears while trying to log in with invalid username")
                self.WriteToLog(self.ResultFile, "FBinvalidUSER Test failed")

        except:
            self.WriteToLog(self.TestFileName, "No error message appears while trying to log in with invalid username")
            self.WriteToLog(self.ResultFile, "FBinvalidUSER Test failed")

        self.driver.quit()



################# main program - use to run from this file #################

#SecondTest = FBinvalidUSER()
#SecondTest.FB_log_in_invalid_username_test()
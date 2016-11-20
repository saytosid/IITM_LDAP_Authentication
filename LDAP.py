#!/usr/bin/python
'''@package IITMandi_LDAP
A Script for IIT Mandi LDAP authentication which is required for internet access.

Requires chromedriver file to be in the same directory or in your $PATH. Set USERNAME and PASSWORD variables in the script.
@author Siddhant Kumar
@date 20 Nov 2016
'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
import subprocess

USERNAME = "Your LDAP username" ##Constant to store your username
PASSWORD = "Your Password" ##Constant to store your password

'''Sets $PATH to include your current working directory'''
def setPATH():
    path = subprocess.check_output("echo $PATH",shell=True)
    os.environ['PATH'] = "PATH="+path+':'+os.getcwd()
    return

'''Initialises a chrome instance'''
def init_driver():
    print "Opening Browser"
    driver = webdriver.Chrome()
    driver.set_window_size(1120, 550)
    print "Waiting..."
    driver.wait = WebDriverWait(driver, 5)
    print "Browser Opened"
    return driver
 
'''Does the job'''
def lookup(driver, un, passw):
    driver.get("http://stgw.iitmandi.ac.in/ug/login.php")
    try:
        username = driver.wait.until(EC.presence_of_element_located(
            (By.NAME, "username")))
        pwd = driver.wait.until(EC.presence_of_element_located(
            (By.NAME, "password")))
        username.send_keys(un)
        pwd.send_keys(passw)
        pwd.submit()
    except TimeoutException:
        print("Box or Button not found")
 
 
if __name__ == "__main__": #Wont be executed if this is included by another script
    output = setPATH()
    driver = init_driver()
    lookup(driver, USERNAME,PASSWORD)
    url = driver.current_url
    while(url.endswith("success.php") != True):
        pass
    driver.quit()

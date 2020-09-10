#
# @file <webchange.py>
#
# @author Fernando Mendiburu - <fernando.mendiburu@ee.ufcg.edu.br>
#

import os
import time
import requests
import difflib
from selenium import webdriver

updateTime = 300 # 5 minutes
path = os.path.expanduser("~") + "/WebChangeFinder/"

#-------------------------------------------------------------------------------------------
#---------------------------------------Functions-------------------------------------------
#-------------------------------------------------------------------------------------------
def InitDriver():
    print('Init driver, headless mode...')
    chromedriver = path + 'chromedriver_linux64/chromedriver'
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("window-size=1200,600")
    driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)
    return driver

def FixAddr(addr):
    substring = "www."
    if not substring in addr:
        addr = substring + addr
    substring = "https://"
    if not substring in addr:
        addr = substring + addr
    return addr

def LoadPage(driver,addr):
    print('Access %s...' % addr)
    driver.get(addr)

def WriteFile(name_file,ResponseContent):
    file = open(name_file,'w+')
    file.write(ResponseContent)
    file.close()

def GetAndSaveResponsePage(file,addr):
    print("Request page...")
    response = requests.get(addr)
    WriteFile(file,response.content)
    print("Page saved!")
    return response

def Prompt(question):
    while "the answer is invalid":
        reply = str(raw_input(question+' (y/n): ')).lower().strip()
        if reply[:1] == 'y':
            return True
        if reply[:1] == 'n':
            return False

def PrintChanges(response_outdated,response_updated):
    isPrint = Prompt("Do you want to print the changes?")
    if(isPrint):
        diff = difflib.ndiff(response_outdated.content.splitlines(), response_updated.content.splitlines())
        print("\n")
        for line in diff:
            if line.startswith('- ') or line.startswith('+ '):
                line = line.replace('\n', '')
                print(line)
        print("\n")

def TakeScreenshot(driver):
    isScreenshot = Prompt("Do you want to take a screenshot?")
    if (isScreenshot):
        driver.save_screenshot("Screenshot.png")

def isMonitoring():
    isMonitor = Prompt("Do you want to continue monitoring the page?\n If (n) the program will end.")
    if (isMonitor): return True
    else: return False

def isValidWebpage(driver):
    try:
        element = driver.find_element_by_xpath("//*[@id='main-message']/h1/span")
        if element.text.find('This site')>=0: return False
        else: return True
    except: return True

def Credits():
    print('-----------------------------------------------------------')
    print('webchange.py: The bot for detecting changes in webpages.')
    print('Fernando Mendiburu - 2020')
    print('-----------------------------------------------------------')

#-------------------------------------------------------------------------------------------
#------------------------------------------Main---------------------------------------------
#-------------------------------------------------------------------------------------------
if __name__ == '__main__':

    try:
        Credits()
        driver = InitDriver()

        CorrectAddr = False
        while not CorrectAddr:
            addr = raw_input("Enter the webpage you want to monitor changes!\nExample https://www.google.com: ")
            addr = FixAddr(addr)
            LoadPage(driver,addr)
            CorrectAddr = isValidWebpage(driver)

        #--- get response ---
        response_outdated = GetAndSaveResponsePage("index_updated.html",addr)

        isMonitor = True
        while isMonitor:
            print("Wait %d seconds to the updated page..." % int(updateTime))
            time.sleep(updateTime)

            #--- get response ---
            response_updated = GetAndSaveResponsePage("index_updated.html",addr)

            if response_outdated.content == response_updated.content:
                print("Webpage without changes!")
            else:
                print("Changes in the webpage!")
                PrintChanges(response_outdated,response_updated)

            isMonitor = isMonitoring()
            if not isMonitor: break

            TakeScreenshot(driver)
            response_outdated = response_updated
            LoadPage(driver,addr)

    except:                     # to handle exceptions better use: TimeoutException, NoSuchElementException, etc
        print("Exception!")

    print("Close Driver\nEnd program!")
    driver.close()

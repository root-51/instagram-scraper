from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()
chrome_options = Options()
chrome_options.add_experimental_option('debuggerAddress','127.0.0.1:9222')
driver = webdriver.Chrome(options=chrome_options)

def getHompage():
    driver.get('https://www.instagram.com/')

def getAccountpage(accountId):
    url = 'https://www.instagram.com/' + str(accountId)
    driver.get(url)
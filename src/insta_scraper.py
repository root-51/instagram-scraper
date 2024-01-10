from enum import Enum
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=chrome_options)


def getHompage():
    driver.get("https://www.instagram.com/")


def getAccountpage(accountId):
    url = "https://www.instagram.com/" + str(accountId)
    driver.get(url)


class InfoType(Enum):
    POST_COUNT = 0
    FOLLOWER_COUNT = 1
    FOLLOWING_COUNT = 2


def getAccountData(data_type: InfoType):
    # POST_COUNT, FOLLOWER_COUNT, FOLLOWING_COUNT
    response_list = driver.find_elements(
        by=webdriver.common.by.By.CSS_SELECTOR, value="span._ac2a"
    )
    data_str = response_list[data_type.value].text
    if "만" in data_str:
        data_str = data_str.replace("만", "")
        data_int = int(float(data_str) * 10000)
        return data_int
    elif "억" in data_str:
        data_str = data_str.replace("억", "")
        data_int = int(float(data_str) * 100000000)
        return data_int
    else:
        return int(data_str)


def getProfileImage():
    response = driver.find_elements(
        by=webdriver.common.by.By.CSS_SELECTOR, value="img.xpdipgo"
    )[1]
    img_src = response.get_attribute("src")
    return str(img_src)

def getAccountName():
    response = driver.find_elements(
        by=webdriver.common.by.By.CSS_SELECTOR, value="span.x1lliihq"
    )[2]
    return str(response.text)
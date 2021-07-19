from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
#initialisong varaibles

PATH = 'C:\\Users\hussa\\Desktop\\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get("https://www.webtalk.co/")

#login
link = driver.find_element_by_link_text("Login")
link.click()

time.sleep(1)

username_textbox = driver.find_element_by_name("userName")
username_textbox.send_keys("hussain28022002@gmail.com")

password_textbox = driver.find_element_by_name("password")
password_textbox.send_keys("Whoami.123")

time.sleep(1)

log = driver.find_element_by_id("signInSubmit")
log.click()

time.sleep(1)

#naviagting to the profile
driver.get("https://www.webtalk.co/hussain.irfan/news")

time.sleep(1)

#like = driver.find_elements_by_xpath('//*[contains(@id, "32218")]/div[1]/div/div/div/span[2]')
#timee = driver.find_elements_by_xpath('//*[contains(@id, "32218")]/div[5]/div/div/ul/li[1]/a/i')
#button = driver.find_elements_by_xpath('//*[contains(@id, "32218")]/div[5]/div/div/ul/li[1]/a')

driver.execute_script("window.scrollBy(0,8000)","")
time.sleep(3)
like = driver.find_elements_by_xpath('//*[contains(@id, "32")]/div[5]/div/div/ul/li[@class="liked-desk like-border-right"]')
driver.execute_script("scrollBy(0,-8000);")
time.sleep(3)
for i in like:
    driver.execute_script("arguments[0].scrollIntoView();",i)
    time.sleep(1)
    driver.execute_script("scrollBy(0,-80);")
    time.sleep(1)
    i.click()




print(like)
time.sleep(5)
ElementClickInterceptedException


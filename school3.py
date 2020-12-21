import requests
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
import time
import smtplib
import ssl
n = 0
check = "niks"
check2 = "niks"
check3 = "niks"
# initiating the webdriver. Parameter includes the path of the webdriver. 
driver = webdriver.Chrome(r"C:\Users\aravr\Downloads\chromedriver_win32\chromedriver.exe")
driver.get(r"https://sghaarlem.magister.net/")
time.sleep(3)
user = driver.find_element_by_id("username")
user.send_keys("***")
login = driver.find_element_by_id("username_submit").click()
time.sleep(1)
user = driver.find_element_by_id("password")
user.send_keys("***")
login = driver.find_element_by_id("password_submit").click()
time.sleep(5)
login = driver.find_element_by_id("menu-cijfers").click()
time.sleep(5)
while n < 1 :
    test = driver.find_element_by_xpath("//td[1]").text
    test2 = driver.find_element_by_xpath("//td[2]").text
    test3 = driver.find_element_by_xpath("//td[4]").text
    if  test != check or test2 != check2 or test3 != check3:
        check = test
        check2 = test2
        check3 = test3
        check4 = check2 + check + check3
        # User configuration
        sender_email = '***'
        receiver_email = '***'
        password = '***'
        server = smtplib.SMTP('smtp.gmail.com', 587)
        # Encrypts the email
        context = ssl.create_default_context()
        server.starttls(context=context)
        # We log in into our Google account
        server.login(sender_email, password)
        # Sending email from sender, to receiver with the email body
        server.sendmail(sender_email, receiver_email, check4)
        server.quit()
    driver.refresh()
    time.sleep(5)


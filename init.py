import rabbitmqMonitor
import timer
import login.webdriver
import logging
logging.basicConfig( filename='coder.log', filemode='a')

#login.webdriver.getcookie(u"170801117",u"06201X")

timer.updateCookie()
timer.getscore()
#监听rabbitmq,写入redis
rabbitmqMonitor.init("1to2session")

#定时任务,每隔30min更新cookie



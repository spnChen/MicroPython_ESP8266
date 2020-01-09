





import network
import utime
import ssd1306
import machine
from machine import RTC, I2C, Pin

import GetTime
import GetWeather
import Chance

First_time = 60000
Second_time = 5000

oled = ssd1306.SSD1306_I2C(128, 64, I2C(scl=Pin(5), sda=Pin(4)))

Led = Pin(2,Pin.OUT)  #将灯点亮，说明开发板运行中
Led.on()
Led.off()


#将WiFi打开
oled.fill(0)
oled.text("Opening The Wifi", 0, 30)
oled.show()
utime.sleep(1)
wlan = network.WLAN(network.STA_IF)
wlan.active(1)
oled.fill(0)

#连接WIFI
oled.text("Connceting",10,30)
oled.text(" to wifi......",0,40)
oled.show()
wlan.connect('LTY','admin666')  #连接网络
oled.fill(0)

while not wlan.isconnected():
  pass

oled.text('Well Connected', 5, 20)  #显示连接是否成功及IP地址
oled.text("IP:" + wlan.ifconfig()[0], 0, 35)
oled.show()
utime.sleep(1)


rtc = RTC()
update_time = utime.ticks_ms() - First_time
print(update_time)

while True:
  if not wlan.isconnected():
    machine.reset()
  
  elif utime.ticks_ms() - update_time >= First_time:
    Year,Month,Day,Hour,Week,Minute,Second = GetTime.Get_Time() #通过GetTime文件爬取时间
    rtc.datetime((Year, Month, Day, Week, Hour, Minute, Second, 0)) #使用RTC实时时钟记录时间
    #date = "{:02}-{:02}-{:02}".format(rtc.datetime()[0], rtc.datetime()[1], rtc.datetime()[2])
    #time = "{:02}:{:02}:{:02}".format(rtc.datetime()[4], rtc.datetime()[5], rtc.datetime()[6])
    Week = Chance.Week_English(rtc.datetime()[3])  #将数字星期变换成英文缩写
    
    Temperature_Now,Temperature_Min,Temperature_Max,Weather = GetWeather.Get_Weather()
    Weather = Chance.Weather_English(Weather)
    
    update_time = utime.ticks_ms()
  
  else:
    update_time = utime.ticks_ms() - First_time + Second_time

  date = "{0}-{1}-{2}".format(rtc.datetime()[0], rtc.datetime()[1], rtc.datetime()[2])  #更新时间
  time = "{:02}:{:02}:{:02}".format(rtc.datetime()[4], rtc.datetime()[5], rtc.datetime()[6])

  Week = Chance.Week_English(rtc.datetime()[3])
  
  oled.fill(0)
  oled.text(date, 5, 0)
  oled.text(Week, 85, 0)
  oled.text(time, 32, 15)
  oled.text("W:" + Weather,15,30)
  oled.text("T:{0}~{1}C".format(Temperature_Min,Temperature_Max),0,45)
  oled.text("NT:" + Temperature_Now +"C", 70, 45)
  oled.show()
  
  utime.sleep(0.1)










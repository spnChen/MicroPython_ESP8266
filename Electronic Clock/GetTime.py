
import urequests
import ujson
import ure

def Get_Time():    #获取天气，温度
  #url = "http://worldtimeapi.org/api/timezone/Asia/ShangHai"
  
  #result = urequests.get(url).text
  #result = ujson.loads(result)
  #time = str(result["datetime"])
  #Year = int(time[0:4])
  #Month = int(time[5:7])
  #Day = int(datetime_str[8:10])
  #Hour = int(datetime_str[11:13])
  #Minute = int(datetime_str[14:16])
  #Second = int(datetime_str[17:19])
  #Week = int(result["day_of_week"])
  
  url = "http://time1909.beijing-time.org/time.asp"
  header={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
  }
  result = urequests.get(url,headers = header).text
  Year = int(ure.search(r'nyear=(.*?);',result).group(1))
  Month = int(ure.search(r'nmonth=(.*?);',result).group(1))
  Day = int(ure.search(r'nday=(.*?);',result).group(1))
  Week = int(ure.search(r'nwday=(.*?);',result).group(1))
  Hour = int(ure.search(r'nhrs=(.*?);',result).group(1))
  Minute = int(ure.search(r'nmin=(.*?);',result).group(1))
  Second = int(ure.search(r'nsec=(.*?);',result).group(1))
  return Year,Month,Day,Hour,Week,Minute,Second











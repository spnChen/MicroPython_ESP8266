

import urequests
import ure

def Get_Space():
  Space_URL = "http://2000019.ip138.com/"
  header={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
  }
  Space = urequests.get(Space_URL,headers = header).text
  Space = ure.search(r'来自：(.*?)市 联通',Space)
  Space = Space.group(1).split("省")[1]
  return Space

def Chance(Space):
  if Space == "绵阳":
    Space = "mianyang"
  elif Space == "南充":
    Space = "nanchong"
  return Space

def Get_Weather():    #获取农历，天气，温度，指数
  #Space = Get_Space()
  #Space = Chance(Space)
  Space = "mianyang"
  URLs = "http://i.tianqi.com/index.php?c=code&a=getcode&id=66&py="+Space

  header = {

    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
    "Upgrade-Insecure-Requests":"1",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cache-Control":"max-age=0",
    "Connection":"keep-alive",
    "Host":"i.tianqi.com"
    }
  result = urequests.get(URLs).text

  result1 = ure.search(r'<span class="t_span">(.*?)</span>',result)
  Temperature_Now = result1.group(1).strip("℃")
  result1 = ure.search(r'<span class="k_span">(.*?)</span>',result)
  Weather = result1.group(1).split(" ")[1]
  Temperature_Min = result1.group(1).split(" ")[0].split("～")[1].strip("℃")
  Temperature_Max = result1.group(1).split(" ")[0].split("～")[0].strip("℃")
  del result,result1
  return Temperature_Now,Temperature_Min,Temperature_Max,Weather









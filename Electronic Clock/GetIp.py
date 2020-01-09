
import random

def ip():
  poxies = {'0':"'https':'101.236.54.97:8866'",
    '1':"'https':'123.163.122.247:9999'",
    '2':"'http':'116.114.19.204:443'",
    '3':"'http':'119.49.241.184:8080'",
    '4':"'http':'52.80.58.248:3128'"
    }
  num = random.randint(0,5)
  print(poxies[str(num)])
  
ip()



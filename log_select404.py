#!/usr/bin/env python
# coding: utf-8

# In[20]:


import random
import re #正则表达式
from faker import Faker #专门生成假数据的库
fake=Faker()
log_entries=[]
status_codes=["200","404","500"]
request_method=["GET","POST"]
#生成1000条日志信息
for i in range(1000):
    ip=fake.ipv4()
    timestamp="10/Oct/2023:13:"
    time=f"{random.randint(0,59):02d}:{random.randint(0,59)}"
    request=f"GET/page.html HTTP/1.1"
    status=random.choice(status_codes)
    size=random.randint(100,10000)
    log_entry=f"{ip}--[{timestamp}{time}] '{request}' {status} {size}"
    log_entries.append(log_entry)
with open("C:\\Users\\86178\\Desktop\\1.log",'w')as f:
    f.write("\n".join(log_entries))
pattern=r"'[^']*' (\d{3}) \d+"
#读取日志：
count=0
with open("C:\\Users\\86178\\Desktop\\1.log",'r')as f:
    #逐行进行读取
    for line in f.readlines():
       match =re.search(pattern,line)
       if match:
           status_code=match.group(1)
           if status_code == '404':
               count+=1 
print("HTTP 404的错误次数是：",count)


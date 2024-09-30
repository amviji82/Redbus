from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

driver=webdriver.Chrome()

driver.get('https://www.redbus.in/bus-tickets/delhi-to-bareilly?fromCityId=733&toCityId=1437&fromCityName=Delhi&toCityName=Bareilly%20(Uttar%20Pradesh)&busType=Any&onward=28-Sep-2024')
time.sleep(3)

driver.find_element(By.CLASS_NAME,"button").click()

searchbox=driver.find_elements(By.CLASS_NAME,"fare")
b=[]
for i in searchbox:
    b.append(i.text)

searchbox=driver.find_elements(By.CLASS_NAME,"bus-type")
c=[]
for i in searchbox:
    c.append(i.text)

searchbox=driver.find_elements(By.CLASS_NAME,"dp-time")
d=[]
for i in searchbox:
    d.append(i.text)

searchbox=driver.find_elements(By.CLASS_NAME,"bp-time")
e=[]
for i in searchbox:
    e.append(i.text)

searchbox=driver.find_elements(By.CLASS_NAME,"dp-loc")
f=[]
for i in searchbox:
    f.append(i.text)

searchbox=driver.find_elements(By.CLASS_NAME,"bp-loc")
g=[]
for i in searchbox:
    g.append(i.text)

searchbox=driver.find_elements(By.CLASS_NAME,"rating-sec")
h=[]
for i in searchbox:
    h.append(i.text)

searchbox=driver.find_elements(By.CLASS_NAME,"seat-left")
j=[]
for i in searchbox:
    j.append(i.text)

K=['APSRTC','APSRTC','APSRTC','APSRTC','APSRTC','APSRTC','APSRTC','APSRTC','APSRTC','APSRTC']


data = {
        "bustype":c,
       "bptime":e,
       "dptime":d,
       "bploc":g,
       "dploc":f,
       "rating":h,
       "fare":b,
       "seatleft":j}

display=pd.DataFrame(data)
print(display)

from sqlalchemy import create_engine
import pandas as pd
#print(display)
host="localhost"
database="database1"
user="postgres"
password="viji"
port="5432"
enginestring=f"postgresql://{user}:{password}@{host}:{port}/{database}"
#enginestring='postgresql+psycopg2://localhost:1234@localhost:5432/database1'
engine=create_engine(enginestring)


s=pd.DataFrame(data)
s.to_sql("redbus9",engine,if_exists='replace',index=False)


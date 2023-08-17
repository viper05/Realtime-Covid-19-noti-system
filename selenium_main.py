from selenium import webdriver
from bs4 import BeautifulSoup
import time
from plyer import notification


def notifyme(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = r"C:\Users\rinku\Desktop\My_code\projects\Realtime-Covid-19-noti-system\favicon.ico",
        timeout = 7
        
    )

driver = webdriver.Chrome('C:\Program Files\Google\Chrome\Application\chromedriver-win64\chromedriver.exe')

driver.get('https://www.mohfw.gov.in/')
content = driver.page_source
# time.sleep(2)
soup = BeautifulSoup(content,'html.parser')
soup.prettify()
# print(soup)
# time.sleep(2)
mydata = []
st = 0
# print(soup.findAll('tbody')[0])
for tr in soup.find_all('tbody'):
    st+=1
    mylist = []   
    for td in tr:
        mylist.append(td.get_text())

    mydata.append(mylist)

    if st >= 36:
        break



# print(mydata)
# #for i in item:
#     #print(i)

states = ['Rajasthan', 'Bihar']
for item in mydata:
    
    #print(item[1])
    if item[1] in states:
        print(item)
        ntitle = 'cases of covid-19'
        ntext = f"State:{item[1]}\nTotal cases:{item[2]}\nCured:{item[4]}\nDeaths:{item[6]}\nActive Last 24 hour:{item[3]}"
        notifyme(ntitle,ntext)
        time.sleep(2)

  
# time.sleep(2)
driver.close()
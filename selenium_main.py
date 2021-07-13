from selenium import webdriver
from bs4 import BeautifulSoup
import time
from plyer import notification


def notifyme(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = r"C:\Users\Rinku\Desktop\py\favicon.ico",
        timeout = 10
        
    )

driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

driver.get('https://www.mohfw.gov.in/')
content = driver.page_source
soup = BeautifulSoup(content,'html.parser')

mydata = []
st = 0
for tr in soup.find_all('tbody')[0]:
    st+=1
    mylist = []   
    for td in tr:
        mylist.append(td.get_text())

    mydata.append(mylist)

    if st >= 36:
        break
    


#for i in item:
    #print(i)

states = ['Rajasthan', 'Uttarakhand']
for item in mydata:
    
    #print(item[1])
    if item[1] in states:
        print(item)
        ntitle = 'cases of covid-19'
        ntext = f"State:{item[1]}\nTotal cases:{item[2]}\nCured:{item[4]}\nDeaths:{item[6]}\nActive Last 24 hour:{item[3]}"
        notifyme(ntitle,ntext)
        time.sleep(2)


driver.close()
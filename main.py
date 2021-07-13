
from plyer import notification
import requests 
from bs4 import BeautifulSoup
import csv
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



def notifyme(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = r"C:\Users\Rinku\Desktop\py\favicon.ico",
        timeout = 10
        
    )

def getdata(url):
    r = requests.get(url)
    return r.text
if __name__ == "__main__":
    # notifyme("Rinku", "Lets stop the virus spread")
    mydata = getdata('https://www.mohfw.gov.in/')
    #driver = webdriver.Chrome()
    #driver.get('https://www.mohfw.gov.in/')
    #content = driver.pagesource

    
    #soup = BeautifulSoup(content)
    soup = BeautifulSoup(mydata, 'html.parser')
    # print(soup.prettify())
    #for table in soup.find_all('table'):
        #print(table.get_text())
    fields = []
    rows = []
    with open('mohfw.csv', 'r') as csvfile:    
        csvreader = csv.reader(csvfile)

        fields = next(csvreader)

        for row in csvreader:
            rows.append(row)

        print("Total no. of rows: %d"%(csvreader.line_num))    

    #
    mydatastr = ""
    for row in rows[:36]:

        for col in row:
            mydatastr += col + '  '
        mydatastr += '\n'

    #mydatastr = ""
    #for tr in soup.find('tbody').find_all('tr'):
    #    mydatastr += tr.get_text()
#
    itemlist = mydatastr.split('\n')

    states = ['Rajasthan', 'Uttarakhand']
    for item in itemlist:
        datalist = item.split('  ')
        #print(datalist[1])
        if datalist[1] in states:
            print(datalist)
            ntitle = 'cases of covid-19'
            ntext = f"State:{datalist[1]}\nTotal cases:{datalist[2]}\nCured:{datalist[4]}\nDeaths:{datalist[6]}\nActive Last 24 hour:{datalist[3]}"
            notifyme(ntitle,ntext)
            time.sleep(2)




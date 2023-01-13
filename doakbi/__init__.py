import requests
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError
from datetime import date
import requests
import os

class bing_download_image:
    def __init__(self,url):       
        self.url=url        
    def myfunc (self):           
        try:
                 matn=requests.get(self.url)    
        except HTTPError as er:
                print('ops! HTTPError')
        except URLError as er:
                print('ops!! URLError')
        Processing_1=BeautifulSoup(matn.text,'html.parser')
        Processing_2=Processing_1.head
        Processing_3=Processing_2.select('link',{'rel':'preload'})[1]
        Processing_4=Processing_3.attrs['href']
        global date    
        today = date.today()
        date = today.strftime("%b-%d-%Y")
        my = os.getcwd() + '/Download Bing Photo'
        newpath = my 
        print(my)
        if not os.path.exists(newpath):
                os.makedirs(newpath)
        response=requests.get(self.url+Processing_4)
        with open (newpath + "/{0}".format(date) + ".jpg",'wb')as file:
                return file.write(response.content)                   
P1=bing_download_image('https://www.bing.com' )
print(P1.myfunc( ))

# ha ha very funny...
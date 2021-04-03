from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError
from datetime import date
import requests
import os


class doakbi():
    def bing(url):        
         try:
             matn=requests.get(url)    
         except HTTPError as er:
            print('ops! HTTPError')
         except URLError as er:
            print('ops!! URLError')
         pardazesh_1=BeautifulSoup(matn.text,'html.parser')
         pardazesh_2=pardazesh_1.head
         pardazesh_3=pardazesh_2.select('link',{'rel':'preload'})[1]
         pardazesh_4=pardazesh_3.attrs['href']
         global date    
         today = date.today()
         date = today.strftime("%b-%d-%Y")
         my = os.getcwd() + '/mamalkhan'
         newpath = my 
         print(my)
         if not os.path.exists(newpath):
            os.makedirs(newpath)
         response=requests.get(url+pardazesh_4)
         with open (newpath + "/{0}".format(date) + ".jpg",'wb')as file:
            return file.write(response.content)
#print(bing('https://www.bing.com'))   


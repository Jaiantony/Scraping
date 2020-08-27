import requests
from twilio.rest import Client 
from bs4 import  BeautifulSoup
account_sid = 'ACb24d633e1c662b499e8a493a1b9c767e' 
auth_token = '3846a54037682bd67a927eda601f7d66' 
client = Client(account_sid, auth_token) 


url="https://www.worldometers.info/coronavirus/country/india/"
res=requests.get(url)
soup=BeautifulSoup(res.text,'html.parser')
soup.prettify()
Today_details= str(soup.title.text)
for new in soup.select(".news_body"):  
    for new in new.find_all("ul",{"class":"news_ul"}):  
        New_cases=new.getText()
        n=New_cases[0:34]
"""message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='{Today_details},{New_cases}'.format(Today_details=Today_details,New_cases=n),
                              to='whatsapp:+919524567504' 
                          ) 
 
print("Message sent",message.sid)"""



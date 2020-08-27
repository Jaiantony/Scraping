import requests
from twilio.rest import Client 
from bs4 import  BeautifulSoup
account_sid = '' 
auth_token = '' 
client = Client(account_sid, auth_token) 


url=""
res=requests.get(url)
soup=BeautifulSoup(res.text,'html.parser')
soup.prettify()
Today_details= str(soup.title.text)
for new in soup.select(".news_body"):  
    for new in new.find_all("ul",{"class":"news_ul"}):  
        New_cases=new.getText()
        n=New_cases[0:34]
message = client.messages.create( 
                              from_='whatsapp:',  
                              body='{Today_details},{New_cases}'.format(Today_details=Today_details,New_cases=n),
                              to='whatsapp:' 
                          ) 
 
print("Message sent",message.sid)



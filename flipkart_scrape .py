import requests
from bs4 import  BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from notify_run import Notify 
import mysql.connector  
#--giving the the desired price of the product
#user_price=int(input("Enter price you deserve to buy the prouct:"))
user_price=1500
msg=f"The Product is lesser than Rs:{user_price}"
#----
#--using BeutifulSoup
url=""
res=requests.get(url)
soup=BeautifulSoup(res.text,'html.parser')
soup.prettify()
title = soup.select('._35KyD6')
price=soup.select('._1uv9Cb') 
spec=soup.select('._3WHvuP')
rating=soup.select('._1i0wk8')
for ratings in rating: #looping inoredr to get rating of the product
   rating=ratings.text
for idx,item in enumerate(title):#extracting the product name and price
   title=title[idx].getText()
   price=price[idx].getText().replace(',','')#replacing the strings
   #str1= ''.join(map(str, price))
   rate=int(price[1:5])
   actual_price=int(price[6:10])
   spec=spec[idx].getText()#   print(rate)
#----
#--Function for sending mail
   def Send_Mail():
    mail_content=(f"The Price of the {title} is reduced from Rs₹:{actual_price} to Rs₹:{user_price},So Go soon and order it in the {url}")
    sender_address = ''
    sender_pass = ''
    receiver_address =('')
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = f'Price of {title} reduced'
    message.attach(MIMEText(mail_content, 'plain'))
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls()
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent Successfully')
#----
#--Function for sending push notification
def Push_Notification():
  notify = Notify()
  notify.send(msg)
  print("Push notification send Succesfully")
#----
#--Function to store the data 
def Store_Data():
  mydb = mysql.connector.connect(
  host="",
  user="",
  passwd="",
  database="")
  mycursor = mydb.cursor()
  #To create  table in database
  #mycursor.execute("CREATE TABLE Product_Details (P_Name VARCHAR(255), P_Price int(10),P_ActualPrice VARCHAR(255),P_Specification VARCHAR(255),P_Rating VARCHAR(255))")
  insert=(
   "INSERT INTO Product_Details(P_Name,P_Price,P_ActualPrice,P_Specification,P_Rating)"
   "VALUES (%s, %s,%s, %s,%s)")#inserting data into table
  data = (title,rate,actual_price,spec,rating)
  mycursor.execute(insert,data)
  mydb.commit()
  print("Data stored Successfully")
#----
#--Comparing the price of the product
if (rate<=user_price):
   Send_Mail()
   Push_Notification()
   Store_Data()
else:
    print(f"Price is not less than Rs₹:{user_price}\n Recheck after some time")
    
    
    
    

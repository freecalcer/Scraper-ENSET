import requests
from bs4 import BeautifulSoup 
import smtplib as sm 
import time 

#the url of the school
URL = "https://www.enset-media.ac.ma/"
#to get your my user agent : write User Agent in google copy it and past it here
Headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}

#function that send send email
def send_Mail():
    server = sm.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("'example.sender@gmail.com'","password")
#login to your email
#better use Two factor auth to generate password or less secure (for gmail )

    subject = "New Thing Add"
    body = f"Check Link : {URL}"
    msg = f"Subject:{subject}\n\n{body}"
    #we define here our message 

    server.sendmail(
        'example.sender@gmail.com',
        'example.receiver@gmail.com',
        msg
    )
    print("Email Has Been Sent")
    server.quit()
    
#function to check if the school add an article 
def check():
    
    page = requests.get(URL, headers = Headers)
    soup= BeautifulSoup(page.content,"html.parser")
    newArticle = soup.find_all("li",class_="new-article")
    #here we bring all the articles that exist in an li with class of new-article
    S = len(newArticle)
    #get how many article we have 
    while(True):
        numberOf = len(newArticle)
        if(S<numberOf):
           S=numberOf
           send_Mail()
           #so here we define a varibale NumberOf that will have also the number of articles with every loop
           #and compare it to the old one if something add the old number of article gonna to change to the new one
           #and an email will be sent to me to inform me that there's a new article by Calling the function send_Mail()
        time.sleep(120)
        #this loop will be repeat every 120 sec

check()

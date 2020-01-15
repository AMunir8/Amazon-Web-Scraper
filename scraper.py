import requests
from bs4 import BeautifulSoup
import smtplib
import time

#product URL
URL = 'https://www.amazon.ca/Magnetic-Erase-Whiteboard-Bulletin-Board/dp/B07GNVZKY2/ref=sr_1_3_sspa?keywords=whiteboard&qid=1578902710&s=office&sr=1-3-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzOE5ZSkFGSDdCOFVDJmVuY3J5cHRlZElkPUEwMDM2ODA4M0dWMEtMWkI1U1hJJmVuY3J5cHRlZEFkSWQ9QTA0MDIwMjQxMEUwMzlMQ0pTQVlBJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'} #obtained by searching for my header on any web browser

def check_price():
    page = requests.get(URL, headers=headers) #obtains the website URL and creates a connection

    soup = BeautifulSoup(page.content, 'html5lib') #used for parsing 

    title = soup.find(id="productTitle").get_text().strip() #Use developer tools on web browser to find the product title div tag and figure out what the id is called
    price = soup.find(id="priceblock_saleprice").get_text().strip()
    converted_price = float(price[5:11]) #converting price from a string to a float

    if(converted_price < 129.99):
        send_mail()

def send_mail(): #sends email if the price reaches lower than $129.99
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('munir2000abdullah@gmail.com', 'reohzvjwgmduumbe') #two step authentication through gmail allows a password for login from various programs

    subject = 'Price has gone down for Specified Product'
    body = 'Check the amazon link https://www.amazon.ca/Magnetic-Erase-Whiteboard-Bulletin-Board/dp/B07GNVZKY2/ref=sr_1_3_sspa?keywords=whiteboard&qid=1578902710&s=office&sr=1-3-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzOE5ZSkFGSDdCOFVDJmVuY3J5cHRlZElkPUEwMDM2ODA4M0dWMEtMWkI1U1hJJmVuY3J5cHRlZEFkSWQ9QTA0MDIwMjQxMEUwMzlMQ0pTQVlBJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'amunir8@uwo.ca',
        'munir.abdullah@outlook.com',
        msg
    )

    print("EMAIL HAS BEEN SENT")
    server.quit()

while(True): #Checks every hour while the program is running 
    check_price()
    time.sleep(60*60)




import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.ca/Magnetic-Erase-Whiteboard-Bulletin-Board/dp/B07GNVZKY2/ref=sr_1_3_sspa?keywords=whiteboard&qid=1578902710&s=office&sr=1-3-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzOE5ZSkFGSDdCOFVDJmVuY3J5cHRlZElkPUEwMDM2ODA4M0dWMEtMWkI1U1hJJmVuY3J5cHRlZEFkSWQ9QTA0MDIwMjQxMEUwMzlMQ0pTQVlBJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html5lib')

    #print(soup.prettify())

    title = soup.find(id="productTitle").get_text().strip()
    price = soup.find(id="priceblock_saleprice").get_text().strip()
    converted_price = float(price[5:11])

    if(converted_price < 129.99):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('munir2000abdullah@gmail.com', 'reohzvjwgmduumbe')

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

while(True):
    check_price()
    time.sleep(60*60)




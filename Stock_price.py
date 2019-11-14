
# Stock Parket price
# When using Email and password please use your own
# Also when using email enable less secure app access from your google account
import bs4
from bs4 import BeautifulSoup
import requests
import smtplib

def parsePrice():
    URL= "https://finance.yahoo.com/quote/BMA?p=BMA&.tsrc=fin-srch"
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' \
                         '(KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'}
    page = requests.get(URL, headers=headers)
    soup= bs4.BeautifulSoup(page.content, 'html.parser')

    price = soup.find('span',{'class':'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}).get_text()
    #return price

# This will continuously updating the price
#while True:
    print('Current Price: '+ str(price))
    if (float(price) > 26):
        send_email(subject, msg)
    elif (float(price) < 26):
        print ('Price is not good to buy right now ')

def send_email(subject, msg):
    try:
        EMAIL_ADDRESS = ("alexnt2357@gmail.com")
        EMAIL_PASSWORD = ("wgbynrdlrcpbmkbk")
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        message = 'subject: {}\n\n{}'.format(subject,msg)
        server.sendmail( EMAIL_ADDRESS,  EMAIL_ADDRESS, message)
        server.quit()
        print("The email has be send!")

    except:
        print('Email failed to send.')

subject = " This price of this stock is good to invest in"
msg = "https://finance.yahoo.com/quote/BMA?p=BMA&.tsrc=fin-srch"




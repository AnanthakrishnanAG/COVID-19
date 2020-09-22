from selenium import webdriver
from twilio.rest import Client
import time



class Coronavirus():

    def  __init__(self):
        chromedriver = 'C:\CHROMEDRIVER\chromedriver'
        self.driver =webdriver.Chrome(chromedriver)

cor=Coronavirus()

def corrun(cor):

    cor.driver.get('https://www.worldometers.info/coronavirus/') #website where we fetch the data about COVID-19 statitics

    deaths=cor.driver.find_elements_by_xpath('//div[@class="maincounter-number"]') # fetching covid death rate
    de=deaths[1]
    det=de.get_attribute("innerHTML")

    print(det[1])
# for GSM message I used a online messageing service twilio create an account at twilio and get your auth details here.
    account_sid = 'ACc4659e54f1c2e431d4be**********' 
    auth_token = '714e7710fcc09eff28453***********'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body=f"Hello this is krish    current corrona death is {det}, so be carefull and stay home",
        from_='+12055********', # this is the from number which twilio give to us for our account
        to='+7962********', # number which we want to send automated message

    )

    print(message.sid)

    return  det
while True:

    corrun(cor)
    time.sleep(60) # give a time lag here appropriate to you. this decide the time interval which you get the message


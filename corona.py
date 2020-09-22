from selenium import webdriver
from twilio.rest import Client
import time



class Coronavirus():

    def  __init__(self):
        chromedriver = 'C:\CHROMEDRIVER\chromedriver'
        self.driver =webdriver.Chrome(chromedriver)

cor=Coronavirus()

def corrun(cor):

    cor.driver.get('https://www.worldometers.info/coronavirus/')

    deaths=cor.driver.find_elements_by_xpath('//div[@class="maincounter-number"]')
    de=deaths[1]
    det=de.get_attribute("innerHTML")

    print(det[1])

    account_sid = 'ACc4659e54f1c2e431d4be17db9acc7904'
    auth_token = '714e7710fcc09eff284533ae465f2e92'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body=f"Hello this is krish    current corrona death is {det}, so be carefull and stay home",
        from_='+12055089903',
        to='+79629634124',

    )

    print(message.sid)

    return  det
while True:

    corrun(cor)
    time.sleep(60)


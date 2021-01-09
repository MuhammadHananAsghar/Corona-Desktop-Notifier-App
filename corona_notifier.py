# Importing Libraries
import datetime
import time 
import requests 
from plyer import notification 


# Getting Data
covidData = None
try:
    covidData = requests.get("https://corona-rest-api.herokuapp.com/Api/pakistan")
except:
    print("Please! Check your internet connection")


# Parsing Data And Giving Notification Every 4 Hours
if (covidData != None):
    data = covidData.json()['Success']
    while(True):
        notification.notify(
            title = "COVID19 Stats on {}".format(datetime.date.today()),
            message = "Total cases : {totalcases}\nToday cases : {todaycases}\nToday deaths :{todaydeaths}\nTotal active :{active}".format(
                        totalcases = data['cases'],
                        todaycases = data['todayCases'],
                        todaydeaths = data['todayDeaths'],
                        active = data["active"]),  
            timeout  = 50
        )
        time.sleep(60*60*4)

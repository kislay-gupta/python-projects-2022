import time

import requests
from datetime import datetime
import smtplib
MY_EMAIL = "dummydownload89@gmail.com"
MY_PASS = "@kimpossible8"
MY_LAT = 25.919300  # Your latitude
MY_LONG = 86.790298  # Your longitude
def iss_is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

def is_night():
    parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True
# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    time.sleep(60)
    if iss_is_overhead() and is_night():
        connection = smtplib.SMTP("smtp.google.com", port=587)
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASS)
        connection.sendmail(from_addr=MY_EMAIL,
                        to_addrs="kislaygupta007@gmail.com",
                        msg="Subject:Look Up\n\nThe ISS is overhead."
                        )
    else:
        print("ISS isn't close")
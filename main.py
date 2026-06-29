from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

URL = "https://amzn.in/d/03teBkS7"
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")
SMTP_ADDRESS = os.environ.get("SMTP_ADDRESS")
HEADER = {"ACCEPT-LANGUAGE":"en-GB,en-US;q=0.9,en;q=0.8","USER-AGENT":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}

response = requests.get(URL, headers=HEADER)

soup = BeautifulSoup(response.text, "html.parser")
name = soup.find(name="span", id="productTitle").getText().split(",")[0]
rupees = soup.find(name="span", class_='a-price-whole').getText()
price = float(soup.find(name="span", class_='a-price-whole').getText().replace(",",""))

if price <= 2550 :
    with smtplib.SMTP(SMTP_ADDRESS, 587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs="rokhit1999@gmail.com", msg=f"Subject:Janu's amazon price tracker\n\n{name} is now available at INR {rupees}.\nHere is the link to buy it:\n{URL}".encode("utf-8"))

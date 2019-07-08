from tkinter import *
from tkinter import ttk

import configparser
import json

import requests

config = configparser.ConfigParser()
config.read("config.ini")

inSymbol = input("moneda")
outSymbol = input("moneda")

url = config["fixer.io"]["RATE_LATEST_EP"]
api_key = config["fixer.io"]["API_KEY"]

url = url.format(api_key, inSymbol, outSymbol)
response = requests.get(url)
if response.status_code == 200:
    currencies = json.loads(response.text)
    print(currencies)
else:
    print("se ha producido un error", response.status_code)
a = 1
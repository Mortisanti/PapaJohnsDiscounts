#TODO Check date of last win, compare to today's date (give or take a day or two)
import requests
from bs4 import BeautifulSoup as BS
from requests.models import Response
from datetime import datetime

"""
# JUST REALIZED THIS WAS USELESS. Use built-in method to determine difference between dates, compare result to 1 or 2 day difference
# Get today's date; do not format as to keep integer values
today = datetime.now()
print(f'{today.month}/{today.day}')

# Get last win date, convert to datetime object so that the values are integers
last_win_date = '03/29 23:30'
last_win_date_converted = datetime.strptime(last_win_date, '%m/%d %H:%M')
print(f'{last_win_date_converted.month}/{last_win_date_converted.day}')
"""

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0'}
url = 'https://betsapi.com/t/57721/MIA-Heat'

def do_stuff():
    src = response.content
    soup = BS(src, 'lxml')

response = requests.get(url, headers=headers)
if response.status_code == 200:
    do_stuff()
else:
    print("No response from webpage.")